# Generated by Django 3.0.4 on 2020-04-08 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200408_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='hackathon_ranking_points',
            field=models.IntegerField(default=0),
        ),
    ]
