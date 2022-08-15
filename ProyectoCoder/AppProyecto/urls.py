from django.urls import path
from .views import *
from AppProyecto.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("list_cliente/", ListCliente.as_view(), name="list_clientes"),
    path("cliente/new/", CreateCliente.as_view(), name="create_clientes"),
    path("cliente/edit/<pk>", UpdateCliente.as_view(), name="update_clientes"),
    path("cliente/delete/<pk>", DeleteCliente.as_view(), name="delete_clientes"),
    path("list_empleado/", ListEmpleado.as_view(), name="list_empleados"),
    path("empleado/new/", CreateEmpleado.as_view(), name="create_empleados"),
    path("empleado/edit/<pk>", UpdateEmpleado.as_view(), name="update_empleados"),
    path("empleado/delete/<pk>", DeleteEmpleado.as_view(), name="delete_empleados"),
    path("list_empresa/", ListEmpresa.as_view(), name="list_empresas"),
    path("empresa/new/", CreateEmpresa.as_view(), name="create_empresas"),
    path("empresa/edit/<pk>", UpdateEmpresa.as_view(), name="update_empresas"),
    path("empresa/delete/<pk>", DeleteEmpresa.as_view(), name="delete_empresas"),
]