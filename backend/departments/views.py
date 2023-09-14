from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAdminUser

from .models import Department
from .serializers import DepartmentSerializer

from core.models import User
from core.serializers import UserSerializer


class GetDepartmentsView(ListAPIView):
    """
    Получение списка всех отделов 
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class GetEmployeeView(ListAPIView):
    """
    Получение списка всех сотрудников. Доступно админу.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class CreateDepartmentView(CreateAPIView):
    """
    Создание отдела. Доступно админу.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdminUser]


class UpdateDepartmentView(UpdateAPIView):
    """
    Редактирование названия, описания, сотрудников отдела. Доступно админу.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdminUser]
 