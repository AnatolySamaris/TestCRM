from django.urls import path

from .views import GetPaymentsView, GetEmployeeStatisticsView, MakePaymentsView


urlpatterns = (
    path("get-payments/", GetPaymentsView.as_view()),
    path("get-employee-statistics/", GetEmployeeStatisticsView.as_view()),
    path("make-payments/", MakePaymentsView.as_view()),
)
