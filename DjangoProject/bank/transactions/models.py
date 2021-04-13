from django.db import models
from django.core.validators import MinValueValidator, MinValueValidator


class Transaction(models.Model):
    transaction_id = models.BigIntegerField(validators=[MinValueValidator(1_00000_00000_0000),
                                                        MinValueValidator(99999_99999_99999)],
                                            primary_key=True)
    time = models.DateTimeField(null=False)
    sender = models.ForeignKey('accounts.Account', null=False, on_delete=models.CASCADE,
                               related_name='%(class)s_sender')
    receiver = models.ForeignKey('accounts.Account', null=False, on_delete=models.CASCADE,
                                 related_name='%(class)s_receiver')
    amount = models.FloatField(null=False)

    def __str__(self):
        return str(self.transaction_id)
