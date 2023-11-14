# Generated by Django 4.2.6 on 2023-11-05 01:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0005_remove_user_is_student_remove_user_is_teacher_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_philomath', models.BooleanField(default=True, verbose_name='philomath status')),
                ('is_tutor', models.BooleanField(default=False, verbose_name='tutor status')),
                ('follows', models.ManyToManyField(blank=True, related_name='followed_by', to='app1.profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]