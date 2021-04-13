# Generated by Django 3.1.7 on 2021-04-09 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=40)),
                ('address', models.CharField(max_length=200)),
                ('registration_date', models.DateField()),
            ],
        ),
    ]