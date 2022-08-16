# Generated by Django 4.0.6 on 2022-08-16 03:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyecto', '0002_rename_clientes_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='fecha',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='cliente',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='blog'),
        ),
    ]
