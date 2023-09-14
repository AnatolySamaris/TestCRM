from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from django.http import FileResponse

from .pdf_creator import PDFApplicationMaker

from .models import Dayoff, Application
from .serializers import DayoffSerializer


class GetDayoffApplicationsList(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Dayoff.objects.all()
    serializer_class = DayoffSerializer


class GetUserDayoffsList(ListAPIView):
    permission_classes = [~IsAdminUser]
    queryset = Dayoff.objects.all()
    serializer_class = DayoffSerializer

    def get_queryset(self):
        try:
            user = self.request.user
            dayoffs = self.queryset.filter(user=user)
            return dayoffs
        except:
            return Response({"message": "Пользователь не найден."}, status=404)


class CreateDayoffApplication(GenericAPIView):
    serializer_class = DayoffSerializer
    permission_classes = [~IsAdminUser]

    def post(self, request):
        try:
            user = request.user
            application_data = request.data
            application_data._mutable = True
            application_data["user_name"] = user.name
        except Exception as e:
            return Response({"message": f"Данные не найдены.\n {e}"})
        template = Application.objects.all().first()    # Предполагается, что имеем только один шаблон (пока что)
        application_maker = PDFApplicationMaker(template)
        application_file = application_maker.make_application(application_data)
        try:
            template = Application.objects.all().first()    # Предполагается, что имеем только один шаблон (пока что)
            application_maker = PDFApplicationMaker(template)
            application_file = application_maker.make_application(application_data)
        except Exception as e:
            return Response({"message": f"Произошла ошибка при создании заявления.\n {e}"})
        
        try:
            Dayoff.objects.create(
                user=user,
                date_from=application_data["date_from"],
                date_to=application_data["date_to"],
                reason=application_data["reason"],
                dayoff_file=application_file
            )
            return Response({"message": "Заявление успешно создано."}, status=200)
        except Exception as e:
            return Response({"message": f"Произошла ошибка при сохранении заявления.\n {e}"})



class DownloadDayoffApplication(RetrieveAPIView):
    queryset = Dayoff.objects.all()
    serializer_class = DayoffSerializer

    def get(self, request, *args, **kwargs):
        dayoff = self.get_object()
        file_path = dayoff.dayoff_file.path 
        response = FileResponse(open(file_path, 'rb'), as_attachment=True)
        return response
