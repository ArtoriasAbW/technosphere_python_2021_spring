from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=80, null=False)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    address = models.CharField(max_length=200)
    registration_date = models.DateField(null=False)

    def __str__(self):
        return self.name


