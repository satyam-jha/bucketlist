# Generated by Django 3.0.7 on 2020-06-19 15:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wish', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishes',
            name='wish_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='wishes',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 19, 21, 3, 36, 52286)),
        ),
    ]
