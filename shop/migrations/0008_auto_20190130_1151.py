# Generated by Django 2.1.5 on 2019-01-30 08:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20190130_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 30, 8, 51, 37, 482135, tzinfo=utc), verbose_name='Дата'),
        ),
    ]
