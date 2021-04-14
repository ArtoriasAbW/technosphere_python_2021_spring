from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Account(models.Model):
    account_number = models.BigIntegerField(verbose_name='Номер счета', validators=[MinValueValidator(1_0000_0000_000),
                                                                                    MaxValueValidator(9999_9999_9999)],
                                            unique=True)
    account_status = models.CharField(verbose_name='Статус счета', max_length=15, null=False)
    client = models.ForeignKey('clients.Client', on_delete=models.SET_NULL, null=True, verbose_name='Клиент')
    account_balance = models.FloatField(verbose_name='Баланс счета', null=False)
    department = models.ForeignKey('departments.Department', on_delete=models.SET_NULL, null=True,
                                   verbose_name='Отделение')
    opening_date = models.DateField(verbose_name='Дата открытия', null=False)

    def __str__(self):
        return str(self.account_number)

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'
