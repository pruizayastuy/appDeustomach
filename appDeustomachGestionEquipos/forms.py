from django import forms
from appDeustomachGestionEquipos.models import Equipo


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
