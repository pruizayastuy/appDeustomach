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
from .views import (EmpleadoListView, EmpleadoDetailView, EmpleadoCreateView, MenuEmpleadosView, listar_empleados,
                    EquipoListView, EquipoDetailView, EquipoCreateView, MenuEquiposView, EquipoDeleteView,
                    listar_equipos, TicketListView, TicketDetailView, TicketCreateView, MenuTicketsView,
                    TicketUpdateView, listar_tickets, SignupView, LoginView, LogoutView)

urlpatterns = [

    # urls de empleados

    path('empleados-index', listar_empleados, name='empleados'),
    path('emplados-menu', MenuEmpleadosView.as_view(), name='empleados_menu'),
    path('empleados-index', EmpleadoListView.as_view(), name='empleados_index'),
    path('empleados-show/<int:pk>', EmpleadoDetailView.as_view(), name='empleados_show'),
    path('empleados-create', EmpleadoCreateView.as_view(), name='empleados_create'),

    # urls de equipos

    path('equipos-index', listar_equipos, name='equipos'),
    path('equipos-menu', MenuEquiposView.as_view(), name='equipos_menu'),
    path('equipos-index', EquipoListView.as_view(), name='equipos_index'),
    path('equipos-show/<int:pk>', EquipoDetailView.as_view(), name='equipos_show'),
    path('equipos-create', EquipoCreateView.as_view(), name='equipos_create'),
    path('equipos-delete', EquipoDeleteView.as_view(), name='equipos_delete'),


    # urls de tickets

    path('tickets-index', listar_tickets, name='tickets'),
    path('tickets-menu', MenuTicketsView.as_view(), name='tickets_menu'),
    path('tickets-index', TicketListView.as_view(), name='tickets_index'),
    path('tickets-show/<int:pk>', TicketDetailView.as_view(), name='tickets_show'),
    path('tickets-create', TicketCreateView.as_view(), name='tickets_create'),
    path('tickets-update/<int:pk>', TicketUpdateView.as_view(), name='tickets_update'),


    # urls de inicio de sesión

    path('signup', SignupView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout')
]
