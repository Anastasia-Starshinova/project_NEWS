# Generated by Django 5.0.3 on 2024-03-22 15:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_alter_appointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 3, 22, 16, 50, 56, 834711)),
        ),
    ]
