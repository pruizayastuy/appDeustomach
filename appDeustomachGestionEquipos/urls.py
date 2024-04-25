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
from django.contrib import admin
from django.urls import path
from . import views
from .views import EquipoListView, EquipoDetailView, EquipoCreateView, EmpleadoListView, EmpleadoDetailView, \
    EmpleadoCreateView

urlpatterns = [
    #url Equipo
    path('/equipos/index', EquipoListView.as_view(), name='equipos_index'),
    path('equipos/show/<int:pk>/', EquipoDetailView.as_view(), name='equipos_show'),
    path('/equipos/create', EquipoCreateView.as_view(), name='equipos_create'),
    #url empleados
    path('/empleados/index', EmpleadoListView.as_view(), name='empleados_index'),
    path('/empleados/show/<int:pk>', EmpleadoDetailView.as_view(), name='empleados_show'),
    path('/empleados/create', EmpleadoCreateView.as_view(), name='empleados_create')
]
