from django.db import models


class Equipo(models.Model):
    numero_serie = models.CharField(max_length=50, unique=True)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    tipo_equipo = models.CharField(max_length=100)
    fecha_adquisicion = models.DateField()
    fecha_puesta_marcha = models.DateField()
    proveedor_nombre = models.CharField(max_length=100)
    proveedor_telefono = models.CharField(max_length=20)
    planta = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.numero_serie} - {self.modelo} ({self.marca})"

    class Meta:
        verbose_name_plural = "equipos"
        verbose_name = "equipo"
        ordering = ["-created"]
