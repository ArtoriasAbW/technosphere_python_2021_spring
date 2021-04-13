# Generated by Django 3.1.7 on 2021-04-09 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210409_1156'),
        ('transactions', '0003_auto_20210409_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_receiver', to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_sender', to='accounts.account'),
        ),
    ]