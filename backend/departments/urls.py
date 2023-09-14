from django.urls import path

from .views import GetDepartmentsView, GetEmployeeView, CreateDepartmentView, UpdateDepartmentView


urlpatterns = (
    path("get-departments/", GetDepartmentsView.as_view()),
    path("get-employee-list/", GetEmployeeView.as_view()),
    path("create-department/", CreateDepartmentView.as_view()),
    path("update-department/<int:pk>", UpdateDepartmentView.as_view()),
)