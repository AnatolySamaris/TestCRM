from django.db import models


class Task(models.Model):
    title = models.CharField(verbose_name="Название задачи", max_length=32)
    short_description = models.CharField(verbose_name="Краткое описание задачи", max_length=64, blank=True)
    description = models.TextField(verbose_name="Подробное описание задачи", max_length=512, blank=True)
    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    deadline = models.DateTimeField(verbose_name="Дедлайн", blank=True)
    hours_cost = models.IntegerField(verbose_name="Стоимость в часах")

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
    
    def __str__(self):
        return self.title
