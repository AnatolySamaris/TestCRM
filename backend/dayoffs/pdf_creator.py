from django.conf import settings

from transliterate import translit

import os, datetime
from PyPDF2 import PdfReader
from fpdf import FPDF


class PDFApplicationMaker:

    def __init__(self, template, line_width=75):
        self.template = template
        self.line_width = line_width


    def __prepare_text(self, text: list) -> list:
        """
        Функция обрабатывает список строк, переписывая их так, чтобы
        в итоговом файле количество слов в строке было соразмерно
        свободному месту в строке.
        """
        words = []  # Собираем список слов из всех строк
        for line in text:
            words.extend(line.split())
        new_text = []
        line = ''
        for word in words:
            if len(line) + len(word) <= self.line_width:
                line += ' ' + word
            else:
                new_text.append(line)
                line = word
        if line: # Если осталась неполная последняя строка
            new_text.append(line)
        return new_text


    def __prepare_data(self, data: dict):
        date_from = datetime.datetime.strptime(data["date_from"], "%Y-%m-%d").date()
        date_to = datetime.datetime.strptime(data["date_to"], "%Y-%m-%d").date()
        prepared_data = {
            "{{company}}": self.template.company_name,
            "{{SEO_name}}": self.template.seo_name,
            "{{employee_name}}": data["user_name"],
            "{{reason}}": data["reason"],
            "{{date_from}}": date_from.strftime("%d.%m.%Y"),
            "{{amount_days}}": str((date_to - date_from).days),
            "{{current_data}}": str(datetime.datetime.today().strftime('%d.%m.%Y'))
        }
        return prepared_data
    

    def make_application(self, data: dict):
        prepared_data = self.__prepare_data(data)

        in_file = PdfReader(self.template.application_file)
        page = in_file.pages[0].extract_text()

        # Подставляем свои данные
        for data_pair in prepared_data.items():
            page = page.replace(*data_pair)
        page = page.split('\n')
        page = list(map(lambda x: x.strip(), page))

        # Обработка текста заявления после строки "Заявление об отгуле"
        page[6:-3] = self.__prepare_text(page[6:-1])

        pdf = FPDF(format='A4')
        pdf.add_page()
        pdf.add_font(
            family='Times',
            fname=os.path.join(settings.MEDIA_ROOT, 'fonts', 'timesnrcyrmt.ttf'),
            uni=True)
        pdf.set_font('times', size=14)

        line = 0
        while 'Заявление' not in page[line]: # До заголовка заявления
            pdf.cell(0, 10, txt=page[line], ln=1, align='R')
            line += 1
        pdf.cell(0, 10, txt=page[line], ln=1, align='C') # Заголовок заявления
        line += 1
        pdf.set_font('times')
        while line != len(page)-1: # Основной текст заявления
            pdf.cell(0, 10, txt=page[line], ln=1, align='L')
            line += 1
        pdf.cell(0, 10, txt=page[line], ln=1, align='R') # Дата и подпись

        filename_namepart = translit(prepared_data["{{employee_name}}"], reversed=True, language_code='ru').replace(' ', '_')
        filename_datepart = str(datetime.datetime.today().strftime("%d_%m_%Y"))
        filename = f"{filename_namepart}_{filename_datepart}.pdf"
        filepath = os.path.join(settings.MEDIA_ROOT, 'dayoffs', filename)

        pdf.output(name=filepath, dest="F")

        return filepath
