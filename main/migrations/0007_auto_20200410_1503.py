# Generated by Django 3.0.4 on 2020-04-10 22:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_profile_hackathon_ranking_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackathon',
            name='id',
            field=models.CharField(default='dwFTcTY4', max_length=8, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='joined_date',
            field=models.DateField(default=datetime.date(2020, 4, 10)),
        ),
    ]
