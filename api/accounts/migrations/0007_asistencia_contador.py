# Generated by Django 5.1.3 on 2024-12-03 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_rename_fecha_asistencia_fecha_asistencia_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='contador',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
