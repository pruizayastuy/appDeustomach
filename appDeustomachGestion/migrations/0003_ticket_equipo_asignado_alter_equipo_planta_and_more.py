# Generated by Django 5.0.4 on 2024-05-24 09:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDeustomachGestion', '0002_proveedor_remove_equipo_proveedor_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='equipo_asignado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appDeustomachGestion.equipo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='equipo',
            name='planta',
            field=models.CharField(choices=[('baja', 'Baja'), ('1', 'Planta 1'), ('2', 'Planta 2'), ('3', 'Planta 3')], default='baja', max_length=100),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='estado_ticket',
            field=models.CharField(choices=[('Abierto', 'Abierto'), ('Cerrado', 'Cerrado'), ('Pausado', 'Pausado')], default='Abierto', max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='nivel_urgencia',
            field=models.CharField(choices=[('Baja', 'Baja'), ('Media', 'Media'), ('Alta', 'Alta')], default='Baja', max_length=50),
        ),
    ]