# Generated by Django 4.2.3 on 2023-07-25 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_demo'),
    ]

    operations = [
        migrations.AddField(
            model_name='demo',
            name='data',
            field=models.JSONField(null=True),
        ),
    ]