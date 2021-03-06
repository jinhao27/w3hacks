# Generated by Django 3.0.4 on 2020-04-08 20:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200408_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathon',
            name='submissions_close_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 8, 20, 47, 12, 727497)),
        ),
        migrations.AddField(
            model_name='hackathon',
            name='submissions_open_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 8, 20, 47, 12, 727478)),
        ),
        migrations.AddField(
            model_name='hackathon',
            name='winners_announced',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 8, 20, 47, 12, 727510)),
        ),
    ]
