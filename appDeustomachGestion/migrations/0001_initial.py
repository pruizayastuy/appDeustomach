# Generated by Django 5.0.4 on 2024-05-22 17:31

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'empleado',
                'verbose_name_plural': 'empleados',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_serie', models.CharField(max_length=50, unique=True)),
                ('modelo', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('tipo_equipo', models.CharField(max_length=100)),
                ('fecha_adquisicion', models.DateField()),
                ('fecha_puesta_marcha', models.DateField()),
                ('proveedor_nombre', models.CharField(max_length=100)),
                ('proveedor_telefono', models.CharField(max_length=20)),
                ('planta', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'equipo',
                'verbose_name_plural': 'equipos',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_referencia', models.CharField(max_length=50, unique=True)),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion_detallada', models.TextField()),
                ('fecha_apertura', models.DateField()),
                ('fecha_resolucion', models.DateField(blank=True, null=True)),
                ('nivel_urgencia', models.CharField(max_length=50)),
                ('tipo_ticket', models.CharField(max_length=50)),
                ('estado_ticket', models.CharField(max_length=50)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('empleado_asignado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appDeustomachGestion.empleado')),
            ],
            options={
                'verbose_name': 'ticket',
                'verbose_name_plural': 'tickets',
                'ordering': ['-created'],
            },
        ),
    ]
