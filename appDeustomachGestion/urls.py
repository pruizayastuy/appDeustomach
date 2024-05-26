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
from .views import (EmpleadoListView, EmpleadoCreateView, MenuEmpleadosView, listar_empleados, EmpleadoUpdateView,
                    EmpleadoDeleteView, EquipoListView, EquipoCreateView, MenuEquiposView, EquipoUpdateView,
                    EquipoDeleteView, listar_equipos, TicketListView, TicketCreateView, MenuTicketsView,
                    TicketUpdateView, TicketDeleteView, listar_tickets, SignupView, LoginView, LogoutView,
                    MenuPrincipalView, TicketDetailAPI, EquipoDetailAPI, EmpleadoDetailAPI, )

urlpatterns = [

    path('', MenuPrincipalView.as_view(), name='menu_principal'),

    # urls de empleados

    path('empleados-menu', listar_empleados, name='empleados'),
    path('emplados-menu', MenuEmpleadosView.as_view(), name='empleados_menu'),
    path('empleados-menu', EmpleadoListView.as_view(), name='empleados_menu'),
    path('empleados-create', EmpleadoCreateView.as_view(), name='empleados_create'),
    path('empleados-update/<int:pk>', EmpleadoUpdateView.as_view(), name='empleados_update'),
    path('empleados-delete/<int:pk>', EmpleadoDeleteView.as_view(), name='empleados_delete'),

    # urls de equipos

    path('equipos-menu', listar_equipos, name='equipos'),
    path('equipos-menu', MenuEquiposView.as_view(), name='equipos_menu'),
    path('equipos-menu', EquipoListView.as_view(), name='equipos_menu'),
    path('equipos-create', EquipoCreateView.as_view(), name='equipos_create'),
    path('equipos-delete/<int:pk>', EquipoDeleteView.as_view(), name='equipos_delete'),
    path('equipos-update/<int:pk>', EquipoUpdateView.as_view(), name='equipos_update'),


    # urls de tickets

    path('tickets-menu', listar_tickets, name='tickets'),
    path('tickets-menu', MenuTicketsView.as_view(), name='tickets_menu'),
    path('tickets-menu', TicketListView.as_view(), name='tickets_menu'),
    path('tickets-create', TicketCreateView.as_view(), name='tickets_create'),
    path('tickets-update/<int:pk>', TicketUpdateView.as_view(), name='tickets_update'),
    path('tickets-delete/<int:pk>', TicketDeleteView.as_view(), name='tickets_delete'),


    # urls de inicio de sesión

    path('signup', SignupView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),

    # urls de API

    path('api/tickets/<int:pk>/', TicketDetailAPI.as_view(), name='ticket_detail_api'),
    path('api/equipos/<int:pk>/', EquipoDetailAPI.as_view(), name='equipo_detail_api'),
    path('api/empleados/<int:pk>/', EmpleadoDetailAPI.as_view(), name='empleado_detail_api')

]
