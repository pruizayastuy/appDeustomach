from django import forms

from appDeustomachGestionEquipos.models import Equipo, Empleado


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'