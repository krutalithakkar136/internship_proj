# Generated by Django 4.2.3 on 2023-07-17 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_mymodel_email_mymodel_name_mymodel_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Click',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.TextField()),
                ('t_desc', models.CharField(max_length=15)),
                ('cat', models.TextField()),
                ('r1', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
