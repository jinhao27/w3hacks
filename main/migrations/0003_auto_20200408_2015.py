# Generated by Django 3.0.4 on 2020-04-08 20:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200407_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='joined_date',
            field=models.DateField(default=datetime.date(2020, 4, 8)),
        ),
    ]