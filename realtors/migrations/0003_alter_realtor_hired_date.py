# Generated by Django 5.1.3 on 2024-11-15 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_alter_realtor_hired_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hired_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 11, 15, 20, 26, 17, 43955)),
        ),
    ]
