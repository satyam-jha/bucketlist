# Generated by Django 3.0.7 on 2020-06-26 08:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wish', '0004_auto_20200626_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishes',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 26, 14, 0, 25, 244202)),
        ),
    ]