from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.ForeignKey(verbose_name="Сотрудник", to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hourly_rate = models.DecimalField(verbose_name="Почасовая ставка, руб.", max_digits=7, decimal_places=2)
    hours = models.IntegerField(verbose_name="Отработанных часов за период", default=0)
    photo = models.ImageField(verbose_name="Фото сотрудника", upload_to='user_images/', null=True, blank=True)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
    
    def __str__(self):
        return self.user.name
