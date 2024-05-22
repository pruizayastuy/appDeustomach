from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from appDeustomachGestion.models import Empleado, Equipo, Ticket


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        labels = {
            'dni': 'DNI',
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'email': 'Email',
            'telefono': 'Teléfono',
        }


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
        labels = {
            'numero_serie': 'Número de serie',
            'modelo': 'Modelo',
            'marca': 'Marca',
            'tipo_equipo': 'Tipo de equipo',
            'fecha_adquisicion': 'Fecha de adquisición',
            'fecha_puesta_marcha': 'Fecha de puesta en marcha',
            'proveedor_nombre': 'Nombre del proveedor',
            'proveedor_telefono': 'Teléfono del proveedor',
            'planta': 'Planta',
        }


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


class TicketSearchForm(forms.Form):
    numero_referencia = forms.CharField(label='Número de referencia', required=False)
    titulo = forms.CharField(label='Título', required=False)


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
