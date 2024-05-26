from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.generic import ListView, View
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

from .models import Empleado, Equipo, Ticket
from .forms import EmpleadoForm, EquipoForm, TicketForm, SignupForm, LoginForm


# Vista general

class MenuPrincipalView(View):
    def get(self, request):
        return render(request, "base.html")


# Vistas de empleados

@method_decorator(login_required(login_url='/appDeustomachGestion/login'), name='dispatch')
class MenuEmpleadosView(View):
    def get(self, request):
        return render(request, "appDeustomachGestionEmpleados/empleados_menu.html")


def listar_empleados(request):
    busqueda = request.POST.get("buscar")
    empleados = Empleado.objects.all()
    if busqueda:
        empleados = Empleado.objects.filter(
            Q(dni__icontains=busqueda) |
            Q(nombre__icontains=busqueda)
        ).distinct()

    return render(request, "appDeustomachGestionEmpleados/empleados_menu.html", {"empleados": empleados})


class EmpleadoDetailAPI(View):
    def get(self, request, pk):
        empleado = get_object_or_404(Empleado, pk=pk)
        data = {
            'nombre': empleado.nombre,
            'apellidos': empleado.apellidos,
            'email': empleado.email,
            'telefono': empleado.telefono,
        }
        return JsonResponse(data)


class EmpleadoListView(ListView):
    model = Empleado
    template_name = "appDeustomachGestionEmpleados/empleados_menu.html"
    context_object_name = "empleados"


class EmpleadoCreateView(View):
    def get(self, request):
        formulario = EmpleadoForm()
        context = {'formulario': formulario}
        return render(request, 'appDeustomachGestionEmpleados/empleados_create.html', context)

    def post(self, request):
        formulario = EmpleadoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('empleados_menu')
        return render(request, 'appDeustomachGestionEmpleados/empleados_create.html', {'formulario': formulario})


class EmpleadoUpdateView(View):
    def get(self, request, pk):
        empleado = Empleado.objects.get(pk=pk)
        formulario = EmpleadoForm(instance=empleado)

        context = {
            'formulario': formulario,
            'empleado': empleado
        }
        return render(request, 'appDeustomachGestionEmpleados/empleados_update.html', context)

    def post(self, request, pk):
        empleado = Empleado.objects.get(pk=pk)
        formulario = EmpleadoForm(request.POST, instance=empleado)
        context = {'formulario': formulario, 'equipo': empleado}

        if formulario.is_valid():
            formulario.save()
            return redirect('empleados_menu')

        return render(request, 'appDeustomachGestionEmpleados/empleados_update.html', context)


class EmpleadoDeleteView(View):
    def get(self, request):
        empleado_id = request.POST.get('empleado_id')
        empleados = get_object_or_404(Empleado, pk=empleado_id)
        return render(request, 'appDeustomachGestionEmpleados/empleados_menu.html', {'empleados': empleados})

    def post(self, request, pk):
        empleado = get_object_or_404(Empleado, pk=pk)
        empleado.delete()
        return redirect('empleados_menu')


# Vistas de equipos


@method_decorator(login_required(login_url='/appDeustomachGestion/login'), name='dispatch')
class MenuEquiposView(View):
    def get(self, request):
        return render(request, "appDeustomachGestionEquipos/equipos_menu.html")


def listar_equipos(request):
    busqueda = request.POST.get("buscar")
    equipos = Equipo.objects.all()
    if busqueda:
        equipos = Equipo.objects.filter(
            Q(numero_serie__icontains=busqueda) |
            Q(modelo__icontains=busqueda)
        ).distinct()

    return render(request, "appDeustomachGestionEquipos/equipos_menu.html", {"equipos": equipos})


class EquipoDetailAPI(View):
    def get(self, request, pk):
        equipo = get_object_or_404(Equipo, pk=pk)
        data = {
            'numero_serie': equipo.numero_serie,
            'modelo': equipo.modelo,
            'marca': equipo.marca,
            'tipo_equipo': equipo.tipo_equipo,
            'fecha_adquisicion': equipo.fecha_adquisicion,
            'fecha_puesta_marcha': equipo.fecha_puesta_marcha,
            'informacion_proveedor': {
                'nombre': equipo.informacion_proveedor.nombre,
                'telefono': equipo.informacion_proveedor.telefono,
            },
            'planta': equipo.planta,
        }
        return JsonResponse(data)


class EquipoListView(ListView):
    model = Equipo
    template_name = "appDeustomachGestionEquipos/equipos_menu.html"
    context_object_name = "equipos"


class EquipoCreateView(View):
    def get(self, request):
        formulario = EquipoForm()
        context = {'formulario': formulario}
        return render(request, 'appDeustomachGestionEquipos/equipos_create.html', context)

    def post(self, request):
        formulario = EquipoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('equipos_menu')
        else:
            context = {'formulario': formulario}
            return render(request, 'appDeustomachGestionEquipos/equipos_create.html', context)


class EquipoUpdateView(View):
    def get(self, request, pk):
        equipo = Equipo.objects.get(pk=pk)
        formulario = EquipoForm(instance=equipo)

        context = {
            'formulario': formulario,
            'equipo': equipo
        }
        return render(request, 'appDeustomachGestionEquipos/equipos_update.html', context)

    def post(self, request, pk):
        equipo = Equipo.objects.get(pk=pk)
        formulario = EquipoForm(request.POST, instance=equipo)
        context = {'formulario': formulario, 'equipo': equipo}

        if formulario.is_valid():
            formulario.save()
            return redirect('equipos_menu')

        return render(request, 'appDeustomachGestionEquipos/equipos_update.html', context)


class EquipoDeleteView(View):
    def get(self, request):
        equipo_id = request.POST.get('equipo_id')
        equipos = get_object_or_404(Equipo, pk=equipo_id)
        return render(request, 'appDeustomachGestionEquipos/equipos_menu.html', {'equipos': equipos})

    def post(self, request, pk):
        equipo = get_object_or_404(Equipo, pk=pk)
        equipo.delete()
        return redirect('equipos_menu')


# Vistas de tickets

@method_decorator(login_required(login_url='/appDeustomachGestion/login'), name='dispatch')
class MenuTicketsView(View):
    def get(self, request):
        return render(request, "appDeustomachGestionTickets/tickets_menu.html")


def listar_tickets(request):
    busqueda = request.POST.get("buscar")
    tickets = Ticket.objects.all()
    if busqueda:
        tickets = Ticket.objects.filter(
            Q(numero_referencia__icontains=busqueda) |
            Q(titulo__icontains=busqueda)
        ).distinct()

    return render(request, "appDeustomachGestionTickets/tickets_menu.html", {"tickets": tickets})


class TicketDetailAPI(View):
    def get(self, request, pk):
        ticket = get_object_or_404(Ticket, pk=pk)
        data = {
            'numero_referencia': ticket.numero_referencia,
            'titulo': ticket.titulo,
            'descripcion_detallada': ticket.descripcion_detallada,
            'fecha_apertura': ticket.fecha_apertura,
            'fecha_resolucion': ticket.fecha_resolucion,
            'nivel_urgencia': ticket.nivel_urgencia,
            'tipo_ticket': ticket.tipo_ticket,
            'estado_ticket': ticket.estado_ticket,
            'empleado_asignado': ticket.empleado_asignado.dni,
            'equipo_asignado': ticket.equipo_asignado.numero_serie,
            'comentarios': ticket.comentarios,
        }
        return JsonResponse(data)


class TicketListView(ListView):
    model = Ticket
    template_name = "appDeustomachGestionTickets/tickets_menu.html"
    context_object_name = "tickets"


class TicketCreateView(View):
    def get(self, request):
        formulario = TicketForm()
        context = {'formulario': formulario}
        return render(request, 'appDeustomachGestionTickets/tickets_create.html', context)

    def post(self, request):
        formulario = TicketForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('tickets_menu'))
        else:
            context = {'formulario': formulario}
            return render(request, 'appDeustomachGestionTickets/tickets_create.html', context)


class TicketUpdateView(View):
    def get(self, request, pk):
        ticket = Ticket.objects.get(pk=pk)
        formulario = TicketForm(instance=ticket)

        context = {
            'formulario': formulario,
            'ticket': ticket
        }
        return render(request, 'appDeustomachGestionTickets/tickets_update.html', context)

    def post(self, request, pk):
        ticket = Ticket.objects.get(pk=pk)
        formulario = TicketForm(request.POST, instance=ticket)
        context = {'formulario': formulario, 'ticket': ticket}

        if formulario.is_valid():
            formulario.save()
            return redirect('tickets_menu')

        return render(request, 'appDeustomachGestionTickets/tickets_update.html', context)


class TicketDeleteView(View):
    def get(self, request):
        ticket_id = request.POST.get('ticket_id')
        tickets = get_object_or_404(Equipo, pk=ticket_id)
        return render(request, 'appDeustomachGestionTickets/tickets_menu.html', {'tickets': tickets})

    def post(self, request, pk):
        ticket = get_object_or_404(Ticket, pk=pk)
        ticket.delete()
        return redirect('tickets_menu')


# Vistas de inicio de sesión

class SignupView(View):
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'appDeustomachInicioSesion/signup.html', {'form': form, 'signup_failed': True})

    def get(self, request):
        form = SignupForm()
        return render(request, 'appDeustomachInicioSesion/signup.html', {'form': form})


class LoginView(View):
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('tickets_menu')
            else:
                return render(request, 'appDeustomachInicioSesion/login.html', {'form': form, 'login_failed': True})
        else:
            return render(request, 'appDeustomachInicioSesion/login.html', {'form': form})

    def get(self, request):
        form = LoginForm()
        return render(request, 'appDeustomachInicioSesion/login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
