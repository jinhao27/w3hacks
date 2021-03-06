# Generated by Django 3.0.4 on 2020-04-13 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20200413_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniexercise',
            name='difficulty_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.DifficultyLevel'),
        ),
        migrations.AlterField(
            model_name='projectexercise',
            name='difficulty_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.DifficultyLevel'),
        ),
        migrations.AlterField(
            model_name='quizexercise',
            name='difficulty_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.DifficultyLevel'),
        ),
    ]
