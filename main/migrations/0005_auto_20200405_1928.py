# Generated by Django 3.0.4 on 2020-04-05 19:28

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200405_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('requirement', models.TextField()),
                ('credits', models.IntegerField()),
                ('ranking_points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('correct_answer_index', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='QuizExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('topic', models.CharField(max_length=50)),
                ('difficulty', models.CharField(max_length=10)),
                ('prerequisites', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=None)),
                ('questions', models.ManyToManyField(to='main.QuizQuestion')),
                ('resources', models.ManyToManyField(to='main.ResourceLink')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('topic', models.CharField(max_length=50)),
                ('difficulty', models.CharField(max_length=10)),
                ('prerequisites', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=None)),
                ('resources', models.ManyToManyField(to='main.ResourceLink')),
            ],
        ),
        migrations.CreateModel(
            name='MiniExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('topic', models.CharField(max_length=50)),
                ('difficulty', models.CharField(max_length=10)),
                ('prerequisites', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=None)),
                ('resources', models.ManyToManyField(to='main.ResourceLink')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='achievements',
            field=models.ManyToManyField(blank=True, to='main.Achievement'),
        ),
    ]
