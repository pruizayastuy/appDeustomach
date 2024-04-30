from django import forms

from appDeustomachGestionEquipos.models import Equipo


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
