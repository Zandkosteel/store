# Generated by Django 2.1.5 on 2019-01-19 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_cartitem_price_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество'),
        ),
    ]
