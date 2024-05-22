from django.db import models
from django.utils import timezone


class Empleado(models.Model):
    dni = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.dni} {self.nombre}"

    class Meta:
        verbose_name_plural = "empleados"
        verbose_name = "empleado"
        ordering = ["-created"]


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
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.numero_serie} - {self.modelo} ({self.marca})"

    class Meta:
        verbose_name_plural = "equipos"
        verbose_name = "equipo"
        ordering = ["-created"]


class Ticket(models.Model):
    numero_referencia = models.CharField(max_length=50, unique=True)
    titulo = models.CharField(max_length=100)
    descripcion_detallada = models.TextField()
    fecha_apertura = models.DateField()
    fecha_resolucion = models.DateField(null=True, blank=True)
    nivel_urgencia = models.CharField(max_length=50)
    tipo_ticket = models.CharField(max_length=50)
    estado_ticket = models.CharField(max_length=50)
    empleado_asignado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    comentarios = models.TextField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.numero_referencia

    class Meta:
        verbose_name_plural = "tickets"
        verbose_name = "ticket"
        ordering = ["-created"]
