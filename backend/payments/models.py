from typing import Iterable, Optional
from django.db import models

from profiles.models import Profile


class Payment(models.Model):
    employee = models.OneToOneField(verbose_name="Сотрудник", to=Profile, on_delete=models.CASCADE)
    amount = models.DecimalField(verbose_name="Размер выплаты, руб.", max_digits=7, decimal_places=2, blank=True)
    payment_date = models.DateField(verbose_name="Дата выплаты", auto_now_add=True)

    class Meta:
        verbose_name = "Выплата"
        verbose_name_plural = "Выплаты"
    
    def __str__(self):
        return f"{self.employee} - {self.amount}"

    def save(self, *args, **kwargs):
        if not self.amount:
            self.amount = self.employee.hourly_rate * self.employee.hours
            self.employee.hours = 0
            self.employee.save()
        return super().save(*args, **kwargs)
