# Generated by Django 4.2.3 on 2023-07-20 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_pract_signup_delete_practice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.TextField()),
                ('f_desc', models.CharField(max_length=30)),
                ('f_modelno', models.IntegerField()),
                ('f_cat', models.TextField()),
            ],
        ),
    ]
