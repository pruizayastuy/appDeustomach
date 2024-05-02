"""
URL configuration for appDeustomachGestionEquipos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.urls import path
from .views import TicketListView, TicketDetailView, TicketCreateView, MenuTicketsView, TicketUpdateView

urlpatterns = [
    path('/tickets/menu', MenuTicketsView.as_view(), name='tickets_menu'),
    path('/tickets/index', TicketListView.as_view(), name='tickets_index'),
    path('/tickets/show/<int:pk>/', TicketDetailView.as_view(), name='tickets_show'),
    path('/tickets/create', TicketCreateView.as_view(), name='tickets_create'),
    path('tickets/update/<int:pk>/', TicketUpdateView.as_view(), name='tickets_update')
]
