from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    birthdate = models.DateField(verbose_name='Дата рождения', null=True)
