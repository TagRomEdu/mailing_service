# Generated by Django 4.2.6 on 2023-11-06 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='mailing_time',
            field=models.TimeField(verbose_name='Время отправки'),
        ),
    ]
