from django.db import models
from appDeustomachGestionEmpleados.models import Empleado
from django.utils import timezone


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

    def save(self, *args, **kwargs):
        if not self.pk:
            # Si es un nuevo objeto, establece el campo created
            self.created = timezone.now()
        self.updated = timezone.now()  # Siempre actualiza el campo updated
        super().save(*args, **kwargs)

    def __str__(self):
        return self.numero_referencia



class Meta:
    verbose_name_plural = "tickets"
    verbose_name = "ticket"
    ordering = ["-created"]
