# Generated by Django 3.0.7 on 2020-06-27 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wish', '0005_auto_20200626_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishes',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 27, 20, 18, 44, 311572)),
        ),
    ]
