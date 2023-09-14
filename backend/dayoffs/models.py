from django.db import models

from core.models import User
from django.conf import settings


class Application(models.Model):
    title = models.CharField(verbose_name="Название заявления", max_length=64)
    company_name = models.CharField(verbose_name="Название компании", max_length=64)
    seo_name = models.CharField(verbose_name="ФИО ген. директора (в дательном падеже)", max_length=128)
    application_file = models.FileField(verbose_name="Файл шаблона", upload_to="application_patterns/")

    class Meta:
        verbose_name = "Шаблон заявления"
        verbose_name_plural = "Шаблоны заявлений"

    def __str__(self):
        return self.title


class Dayoff(models.Model):
    user = models.ForeignKey(verbose_name="Сотрудник", to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_from = models.DateField(verbose_name="Дата от")
    date_to = models.DateField(verbose_name="Дата до")
    reason = models.TextField(verbose_name="Причина отгула", max_length=256)
    dayoff_file = models.FileField(verbose_name="Файл заявления", upload_to="dayoffs/", blank=True, null=True)

    class Meta:
        verbose_name = "Заявление на отгул"
        verbose_name_plural = "Заявления на отгул"
    
    def __str__(self):
        return f"{self.user} ({self.date_from} - {self.date_to})"
