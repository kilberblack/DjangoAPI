# Generated by Django 5.1.3 on 2024-12-03 06:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_asistencia_estado_asistencia_contador'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='asistencia',
            old_name='fecha',
            new_name='fecha_asistencia',
        ),
        migrations.RemoveField(
            model_name='asignatura',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='asistencia',
            name='contador',
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='descripcion',
            field=models.TextField(default='Sin descripcion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='asignatura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.asignatura'),
        ),
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asignaturas', models.ManyToManyField(through='accounts.Asistencia', to='accounts.asignatura')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.perfilusuario'),
        ),
    ]
