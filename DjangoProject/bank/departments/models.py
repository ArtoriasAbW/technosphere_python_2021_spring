from django.db import models


class Department(models.Model):
    name = models.CharField(verbose_name='Название', max_length=80, null=False)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=20)
    address = models.CharField(verbose_name='Адрес', max_length=200)
    user = models.ForeignKey('users.CustomUser', on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Отделение'
        verbose_name_plural = 'Отделения'
