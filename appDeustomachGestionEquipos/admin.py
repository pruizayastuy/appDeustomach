from django.contrib import admin

from appDeustomachGestionEquipos.models import Equipo, Empleado, Ticket

# Register your models here.
admin.site.register(Equipo)
admin.site.register(Empleado)
admin.site.register(Ticket)
