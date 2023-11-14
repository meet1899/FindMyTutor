# Generated by Django 4.2.6 on 2023-11-04 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_question_owner_remove_question_solvedby_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_student',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_teacher',
        ),
        migrations.AddField(
            model_name='user',
            name='is_philomath',
            field=models.BooleanField(default=False, verbose_name='philomath status'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_tutor',
            field=models.BooleanField(default=False, verbose_name='tutor status'),
        ),
    ]