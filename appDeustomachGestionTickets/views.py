from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from appDeustomachGestionTickets.models import Ticket, Empleado
from appDeustomachGestionTickets.forms import TicketForm
from django.views.generic import ListView, DetailView, View, UpdateView


class MenuTicketsView(View):
    def get(self, request):
        return render(request, "appDeustomachGestionTickets/tickets_menu.html")


class TicketListView(ListView):
    model = Ticket
    template_name = "appDeustomachGestionTickets/tickets_index.html"
    context_object_name = "tickets"


class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'appDeustomachGestionTickets/tickets_detail.html'
    context_object_name = 'ticket'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ticket = self.get_object()
        empleado_asignado = ticket.empleado_asignado
        if empleado_asignado:
            context['empleado_asignado'] = empleado_asignado
        return context


class TicketCreateView(View):
    def get(self, request):
        formulario = TicketForm()
        context = {'formulario': formulario}
        return render(request, 'appDeustomachGestionTickets/tickets_create.html', context)

    def post(self, request):
        ticket_id = request.POST.get('ticket_id')
        ticket = Ticket.objects.get(pk=ticket_id)
        formulario = TicketForm(request.POST, instance=ticket)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(reverse('tickets_index'))  # Redirigir a la lista de tickets después de actualizar
        else:
            context = {'formulario': formulario}
            return render(request, 'appDeustomachGestionTickets/tickets_update.html', context)


class TicketUpdateView(View):
    def get(self, request):
        tickets = Ticket.objects.all()
        context = {'tickets': tickets}
        return render(request, 'appDeustomachGestionTickets/tickets_update.html', context)

    def post(self, request):
        ticket_id = request.POST.get('ticket_id')
        ticket = Ticket.objects.get(pk=ticket_id)
        formulario = TicketForm(instance=ticket)
        context = {'formulario': formulario}

        if formulario.is_valid():
            formulario.save()
            return redirect('tickets_index')

        return render(request, 'appDeustomachGestionTickets/tickets_update.html', context)
