# Generated by Django 4.2.6 on 2023-11-06 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_profile_facebook_link_profile_homepage_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='tutor_field',
            field=models.CharField(default='Nothing yet!', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_philomath',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='philomath status'),
        ),
    ]