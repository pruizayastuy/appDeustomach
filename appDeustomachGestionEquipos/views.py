from django.shortcuts import render, get_object_or_404
from appEmpresaDeustomach.models import Equipo, Empleado, Ticket
from django.views.generic import ListView, DetailView, View, DeleteView, UpdateView


class EquipoListView(ListView):
    model = Equipo
    template_name = "appEmpresaDeustomach/equipos_index.html"
    context_object_name = "equipos"


class EquipoDetailView(DetailView):
    model = Equipo
    template_name = "appEmpresaDeustomach/equipo_detail.html"
    context_object_name = "equipo"