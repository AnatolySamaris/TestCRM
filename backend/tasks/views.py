from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer, TaskDetailSerializer

from departments.models import DepartmentMember, Department
from departments.serializers import DepartmentTasksSerializer

from profiles.models import Profile


class GetAllTasksView(ListAPIView):
    """
    Для вывода всех задач по отделам. Доступно админу.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentTasksSerializer
    permission_classes = [IsAdminUser]


class GetDepartmentTasksView(ListAPIView):
    """
    Для вывода задач отдела сотрудника. Доступно только сотруднику.
    """
    serializer_class = TaskSerializer
    permission_classes = [~IsAdminUser]

    def get_queryset(self):
        try:
            user = self.request.user
            user_department = Department.objects.get(members__user=user)
            untaken_tasks = user_department.tasks.exclude(
                id__in=DepartmentMember.objects.all().values_list('tasks__id')
            )
            return untaken_tasks
        except:
            return Task.objects.none()


class GetUserTasksView(ListAPIView):
    """
    Для вывода задач сотрудника. Доступно только сотруднику.
    """
    serializer_class = TaskSerializer
    permission_classes = [~IsAdminUser]

    def get_queryset(self):
        try:
            user = self.request.user
            employee = DepartmentMember.objects.get(user=user)
            return employee.tasks
        except:
            return Task.objects.none()


class ShowTaskDetailsView(GenericAPIView):
    """
    Показать детальное описание задачи. Доступно всем.
    """
    def get(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
            task_serializer = TaskDetailSerializer(task)
            return Response(task_serializer.data, status=200)
        except Exception as e:
            return Response({"message": f"Задача не найдена.\n {e}"}, status=404)


class TakeTaskView(GenericAPIView):
    """
    Взять задачу на себя. Доступно только сотруднику.
    """
    permission_classes = [~IsAdminUser]

    def post(self, request, task_id):
        try:
            user = request.user
            employee = DepartmentMember.objects.get(user=user)
            task = Task.objects.get(id=task_id)
        except Exception as e:
            return Response({"message": f"Пользователь или задача не найдены.\n {e}"})
        
        try:
            employee.tasks.add(task)
            return Response({"message": "Задача успешно взята."}, status=200)
        except Exception as e:
            return Response({"message": f"Не получилось добавить задачу.\n {e}"})


class CompleteTaskView(GenericAPIView):
    """
    Закрыть задачу, получив на счет указанные часы. Доступно только сотруднику.
    """
    permission_classes = [~IsAdminUser]

    def delete(self, request, task_id):
        try:
            user = request.user
            employee = DepartmentMember.objects.get(user=user)
            task = employee.tasks.get(id=task_id)
        except Exception as e:
            return Response({"message": f"Пользователь или задача не найдены.\n {e}"})
        
        try:
            user_profile = Profile.objects.get(user=employee.user)
            user_profile.hours += task.hours_cost
            user_profile.save()
            employee.tasks.remove(task)
            task.delete()
            return Response({"message": "Задача успешно закрыта."}, status=200)
        except Exception as e:
            return Response({"message": f"Не получилось закрыть задачу.\n {e}"})
