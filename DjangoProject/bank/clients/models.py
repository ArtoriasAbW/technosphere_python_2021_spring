from django.db import models


class Client(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=80, null=False)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=20)
    email = models.EmailField(verbose_name='email', max_length=40)
    address = models.CharField(verbose_name='Адрес', max_length=200)
    registration_date = models.DateField(verbose_name='Дата регистрации', null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', '-registration_date']
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


