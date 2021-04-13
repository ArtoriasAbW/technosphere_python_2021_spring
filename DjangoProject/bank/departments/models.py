from django.db import models


class Department(models.Model):

    name = models.CharField(max_length=80, null=False)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
