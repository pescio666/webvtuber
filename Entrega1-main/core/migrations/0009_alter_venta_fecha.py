# Generated by Django 4.2.1 on 2024-06-27 21:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_venta_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 27, 17, 54, 35, 154599)),
        ),
    ]
