from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator

from appDeustomachGestionEquipos.models import Equipo
from appDeustomachGestionEquipos.forms import EquipoForm
from django.views.generic import ListView, DetailView, View


@method_decorator(login_required(login_url='/appDeustomachInicioSesion/login/'), name='dispatch')
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


class EquipoDeleteView(View):
    def get(self, request):
        equipos = Equipo.objects.all()
        return render(request, 'appDeustomachGestionEquipos/equipos_delete.html', {'equipos': equipos})

    def post(self, request):
        equipo_id = request.POST.get('equipo_id')
        equipo = get_object_or_404(Equipo, pk=equipo_id)
        equipo.delete()
        return redirect('equipos_index')
