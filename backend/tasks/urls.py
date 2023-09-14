from django.urls import path

from .views import (
    GetAllTasksView, 
    GetUserTasksView, 
    GetDepartmentTasksView, 
    ShowTaskDetailsView, 
    TakeTaskView, 
    CompleteTaskView
)


urlpatterns = (
    path("get-all-tasks/", GetAllTasksView.as_view()),
    path("get-user-tasks/", GetUserTasksView.as_view()),
    path("get-department-tasks/", GetDepartmentTasksView.as_view()),
    path("show-task-details/<int:task_id>", ShowTaskDetailsView.as_view()),
    path("take-task/<int:task_id>", TakeTaskView.as_view()),
    path("complete-task/<int:task_id>", CompleteTaskView.as_view()),
)