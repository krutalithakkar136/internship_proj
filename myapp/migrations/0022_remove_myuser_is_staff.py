# Generated by Django 4.2.3 on 2023-07-31 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_myuser_is_staff_myuser_is_superuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_staff',
        ),
    ]
