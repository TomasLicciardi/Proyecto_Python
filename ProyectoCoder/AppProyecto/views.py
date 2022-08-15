from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import UpdateView, ListView, DeleteView, CreateView
from django.urls import reverse_lazy

# Create your views here.

def inicio(request):
    return render(request, "AppProyecto/index.html")

class ListCliente(ListView):
    model = Cliente
    template_name = "AppProyecto/list_clientes.html"

class CreateCliente(CreateView):
    model = Cliente
    success_url = reverse_lazy("inicio")
    fields = ["nombre", "apellido", "direccion", "edad"]

class UpdateCliente(UpdateView):
    model = Cliente
    success_url = reverse_lazy("inicio")
    fields = ["nombre", "apellido", "direccion", "edad"]

class DeleteCliente(DeleteView):
    model = Cliente
    success_url = reverse_lazy("inicio")

class ListEmpleado(ListView):
    model = Empleado
    template_name = "AppProyecto/list_empleados.html"

class CreateEmpleado(CreateView):
    model = Empleado
    success_url = reverse_lazy("inicio")
    fields = ["nombre", "apellido", "salario", "edad"]

class UpdateEmpleado(UpdateView):
    model = Empleado
    success_url = reverse_lazy("inicio")
    fields = ["nombre", "apellido", "salario", "edad"]

class DeleteEmpleado(DeleteView):
    model = Empleado
    success_url = reverse_lazy("inicio")

class ListEmpresa(ListView):
    model = Empresa
    template_name = "AppProyecto/list_empresas.html"

class CreateEmpresa(CreateView):
    model = Empresa
    success_url = reverse_lazy("inicio")
    fields = ["nombre", "direccion"]

class UpdateEmpresa(UpdateView):
    model = Empresa
    success_url = reverse_lazy("inicio")
    fields = ["nombre", "direccion"]

class DeleteEmpresa(DeleteView):
    model = Empresa
    success_url = reverse_lazy("inicio")