# Generated by Django 4.2.3 on 2023-07-31 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_remove_myuser_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
