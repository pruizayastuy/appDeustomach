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


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.telefono}"

    class Meta:
        verbose_name_plural = "proveedores"
        verbose_name = "proveedor"
        ordering = ["-created"]


class Equipo(models.Model):
    PLANTA_CHOICES = [
        ('baja', 'Baja'),
        ('1', 'Planta 1'),
        ('2', 'Planta 2'),
        ('3', 'Planta 3'),
    ]

    numero_serie = models.CharField(max_length=50, unique=True)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    tipo_equipo = models.CharField(max_length=100)
    fecha_adquisicion = models.DateField()
    fecha_puesta_marcha = models.DateField()
    informacion_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    planta = models.CharField(max_length=100, choices=PLANTA_CHOICES, default='baja')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.numero_serie})"

    class Meta:
        verbose_name_plural = "equipos"
        verbose_name = "equipo"
        ordering = ["-created"]


class Ticket(models.Model):
    NIVEL_URGENCIA = [
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta')
    ]
    ESTADO_TICKET = [
        ('Abierto', 'Abierto'),
        ('Cerrado', 'Cerrado'),
        ('Pausado', 'Pausado')
    ]
    numero_referencia = models.CharField(max_length=50, unique=True)
    titulo = models.CharField(max_length=100)
    descripcion_detallada = models.TextField()
    fecha_apertura = models.DateField()
    fecha_resolucion = models.DateField(null=True, blank=True)
    nivel_urgencia = models.CharField(max_length=50, choices=NIVEL_URGENCIA, default='Baja')
    tipo_ticket = models.CharField(max_length=50)
    estado_ticket = models.CharField(max_length=50, choices=ESTADO_TICKET, default='Abierto')
    empleado_asignado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    equipo_asignado = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    comentarios = models.TextField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.numero_referencia

    class Meta:
        verbose_name_plural = "tickets"
        verbose_name = "ticket"
        ordering = ["-created"]
