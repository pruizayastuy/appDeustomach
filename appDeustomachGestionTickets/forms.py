from django import forms

from appDeustomachGestionTickets.models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
