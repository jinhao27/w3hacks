# Generated by Django 3.0.4 on 2020-04-17 21:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20200415_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='joined_date',
            field=models.DateField(default=datetime.date(2020, 4, 17)),
        ),
        migrations.CreateModel(
            name='CompletedProjectExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github_link', models.CharField(max_length=100)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('project_exercise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.ProjectExercise')),
            ],
        ),
    ]
