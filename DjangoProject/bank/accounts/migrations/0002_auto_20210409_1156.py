# Generated by Django 3.1.7 on 2021-04-09 11:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.BigIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(15), django.core.validators.MaxLengthValidator(15)]),
        ),
    ]
