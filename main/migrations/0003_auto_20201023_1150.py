# Generated by Django 2.1.4 on 2020-10-23 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201023_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 23, 11, 50, 6, 873385), verbose_name='date published'),
        ),
    ]
