from django.urls import path

from .views import (
    GetDayoffApplicationsList,
    GetUserDayoffsList,
    CreateDayoffApplication,
    DownloadDayoffApplication
)

urlpatterns = (
    path("get-dayoffs-list/", GetDayoffApplicationsList.as_view()),
    path("get-user-dayoffs/", GetUserDayoffsList.as_view()),
    path("create-dayoff/", CreateDayoffApplication.as_view()),
    path("download-dayoff/<int:pk>", DownloadDayoffApplication.as_view()),
)
