from django.db import models
from django.conf import settings

from core.models import User
from tasks.models import Task


class DepartmentMember(models.Model):
    user = models.ForeignKey(verbose_name="Сотрудник", to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    position = models.CharField(verbose_name="Должность", max_length=32)
    tasks = models.ManyToManyField(verbose_name="Выполняемые задачи", to=Task, blank=True)

    class Meta:
        verbose_name = "Сотрудник отдела"
        verbose_name_plural = "Сотрудники отдела"
    
    def __str__(self):
        return f"{self.user.name} ({self.position})"


class Department(models.Model):
    title = models.CharField(verbose_name="Название отдела", max_length=64)
    description = models.CharField(verbose_name="Описание отдела", max_length=256)
    members = models.ManyToManyField(verbose_name="Сотрудники отдела", to=DepartmentMember, blank=True, null=True)
    tasks = models.ManyToManyField(verbose_name="Задачи в отделе", to=Task, blank=True)

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"
    
    def __str__(self):
        return self.title
