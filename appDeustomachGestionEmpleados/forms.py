from django import forms
from appDeustomachGestionEmpleados.models import Empleado


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
