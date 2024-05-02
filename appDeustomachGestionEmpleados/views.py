from django.shortcuts import render, redirect
from appDeustomachGestionEmpleados.models import Empleado
from appDeustomachGestionEmpleados.forms import EmpleadoForm
from django.views.generic import ListView, DetailView, View


class MenuEmpleadosView(View):
    def get(self, request):
        return render(request, "appDeustomachGestionEmpleados/empleados_menu.html")


class EmpleadoListView(ListView):
    model = Empleado
    template_name = "appDeustomachGestionEmpleados/empleados_index.html"
    context_object_name = "empleados"


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "appDeustomachGestionEmpleados/empleados_detail.html"
    context_object_name = "empleado"


class EmpleadoCreateView(View):
    def get(self, request):
        formulario = EmpleadoForm()
        context = {'formulario': formulario}
        return render(request, 'appDeustomachGestionEmpleados/empleados_create.html', context)

    def post(self, request):
        formulario = EmpleadoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('empleados_index')
        return render(request, 'appDeustomachGestionEmpleados/empleados_create.html', {'formulario': formulario})
