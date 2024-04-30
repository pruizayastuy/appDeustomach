from django.db import models


class Empleado(models.Model):
    dni = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.dni} {self.nombre}"

    class Meta:
        verbose_name_plural = "empleados"
        verbose_name = "empleado"
        ordering = ["-created"]
