from django import forms
from appDeustomachGestionTickets.models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        labels = {
            'numero_referencia': 'Número de referencia',
            'titulo': 'Título',
            'descripcion_detallada': 'Descripción detallada',
            'fecha_apertura': 'Fecha de apertura',
            'fecha_resolucion': 'Fecha de resolución',
            'nivel_urgencia': 'Nivel de urgencia',
            'tipo_ticket': 'Tipo de ticket',
            'estado_ticket': 'Estado del ticket',
            'empleado_asignado': 'Empleado asignado',
            'comentarios': 'Comentarios',
        }
