from django.db import models
from django.contrib.auth import models as authmodels


class User(authmodels.AbstractUser):
    first_name = None
    last_name = None

    name = models.CharField("Ф.И.О.", max_length=256, blank=True)
