# Generated by Django 4.2.1 on 2024-06-27 03:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_producto_precio_alter_venta_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(max_length=3),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 26, 23, 43, 45, 233752)),
        ),
    ]
