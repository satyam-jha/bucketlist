# Generated by Django 3.0.7 on 2020-06-26 08:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wish', '0002_auto_20200619_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishes',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 26, 13, 55, 31, 72078)),
        ),
    ]
