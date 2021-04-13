from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Account(models.Model):
    account_number = models.BigIntegerField(validators=[MinValueValidator(1_0000_0000_000),
                                                        MaxValueValidator(9999_9999_9999)],
                                            primary_key=True)
    account_status = models.CharField(max_length=15, null=False)
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE, null=False)
    account_balance = models.FloatField(null=False)
    department = models.ForeignKey('departments.Department', on_delete=models.CASCADE, null=False)
    opening_date = models.DateField(null=False)

    def __str__(self):
        return str(self.account_number)
