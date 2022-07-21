from django.urls import path
from .views import *
from AppProyecto.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("empleados/", empleados, name="empleados"),
    path("empresa/", empresa, name="empresa"),
    path("clientes/", clientes, name="clientes"),
    path("busqueda_clientes/", buscar_clientes, name="busqueda_clientes"),
    path("resultado_clientes/", resultado_clientes, name="resultado_clientes"),
]