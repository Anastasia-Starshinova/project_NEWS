# Generated by Django 5.0.3 on 2024-03-25 14:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2024, 3, 25, 15, 59, 42, 877395))),
                ('client_name', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
