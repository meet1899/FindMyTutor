# Generated by Django 4.2.6 on 2023-11-10 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0023_alter_profile_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_link',
            field=models.CharField(default='', max_length=500),
        ),
    ]
