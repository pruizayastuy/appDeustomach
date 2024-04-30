from django.shortcuts import render, get_object_or_404, redirect
from appDeustomachGestionTickets.models import Ticket, Empleado
from appDeustomachGestionTickets.forms import TicketForm
from django.views.generic import ListView, DetailView, View


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
        formulario = TicketForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('tickets_index')
        return render(request, 'appDeustomachGestionTickets/tickets_create.html', {'formulario': formulario})
