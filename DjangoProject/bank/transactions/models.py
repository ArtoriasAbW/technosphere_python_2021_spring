from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Transaction(models.Model):
    transaction_id = models.BigIntegerField(verbose_name='Идентификатор транзакции',
                                            validators=[MinValueValidator(1_00000_00000_0000),
                                                        MaxValueValidator(99999_99999_99999)],
                                            unique=True)
    time = models.DateTimeField(null=False)
    sender = models.ForeignKey('accounts.Account', null=True, on_delete=models.SET_NULL,
                               related_name='%(class)s_sender', verbose_name='Отправитель')
    receiver = models.ForeignKey('accounts.Account', null=True, on_delete=models.SET_NULL,
                                 related_name='%(class)s_receiver', verbose_name='Получатель')
    amount = models.FloatField(null=False, verbose_name='Сумма транзакции')

    def __str__(self):
        return str(self.transaction_id)

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
