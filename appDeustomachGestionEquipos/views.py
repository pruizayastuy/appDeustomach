from django.shortcuts import render, get_object_or_404, redirect
from appDeustomachGestionEquipos.models import Equipo
from appDeustomachGestionEquipos.forms import EquipoForm
from django.views.generic import ListView, DetailView, View


class MenuEquiposView(View):
    def get(self, request):
        return render(request, "appDeustomachGestionEquipos/equipos_menu.html")


class EquipoListView(ListView):
    model = Equipo
    template_name = "appDeustomachGestionEquipos/equipos_index.html"
    context_object_name = "equipos"


class EquipoDetailView(DetailView):
    model = Equipo
    template_name = "appDeustomachGestionEquipos/equipos_detail.html"
    context_object_name = "equipo"


class EquipoCreateView(View):
    def get(self, request):
        formulario = EquipoForm()
        context = {'formulario': formulario}
        return render(request, 'appDeustomachGestionEquipos/equipos_create.html', context)

    def post(self, request):
        formulario = EquipoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('equipos_index')
        return render(request, 'appDeustomachGestionEquipos/equipos_create.html', {'formulario': formulario})
