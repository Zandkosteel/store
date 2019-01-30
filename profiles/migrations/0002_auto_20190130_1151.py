# Generated by Django 2.1.5 on 2019-01-30 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.SET_NULL, to='country.City', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.SET_NULL, to='country.Country', verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(default=79000000000, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.SET_NULL, to='country.State', verbose_name='Республика/Штат'),
        ),
    ]