# Generated by Django 4.2.6 on 2023-11-08 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_hire_req'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_bio',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]