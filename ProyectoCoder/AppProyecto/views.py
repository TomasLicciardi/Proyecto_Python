from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import UpdateView, ListView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ListCliente(ListView, LoginRequiredMixin):
    model = Cliente
    template_name = "AppProyecto/list_clientes.html"

class CreateCliente(CreateView, LoginRequiredMixin):
    model = Cliente
    success_url = reverse_lazy("inicio")
    fields = ["nombre", "apellido", "direccion", "edad"]

class UpdateCliente(UpdateView, LoginRequiredMixin):
    model = Cliente
    success_url = reverse_lazy("inicio")
    fields = ["nombre", "apellido", "direccion", "edad"]

class DeleteCliente(DeleteView, LoginRequiredMixin):
    model = Cliente
    success_url = reverse_lazy("inicio")

class ListEmpleado(ListView, LoginRequiredMixin):
    model = Empleado
    template_name = "AppProyecto/list_empleados.html"

class CreateEmpleado(CreateView, LoginRequiredMixin):
    model = Empleado
    success_url = reverse_lazy("inicio")
    fields = ["nombre", "apellido", "salario", "edad"]

class UpdateEmpleado(UpdateView, LoginRequiredMixin):
    model = Empleado
    success_url = reverse_lazy("inicio")
    fields = ["nombre", "apellido", "salario", "edad"]

class DeleteEmpleado(DeleteView, LoginRequiredMixin):
    model = Empleado
    success_url = reverse_lazy("inicio")

class ListEmpresa(ListView, LoginRequiredMixin):
    model = Empresa
    template_name = "AppProyecto/list_empresas.html"

class CreateEmpresa(CreateView, LoginRequiredMixin):
    model = Empresa
    success_url = reverse_lazy("inicio")
    fields = ["nombre", "direccion"]

class UpdateEmpresa(UpdateView, LoginRequiredMixin):
    model = Empresa
    success_url = reverse_lazy("inicio")
    fields = ["nombre", "direccion"]

class DeleteEmpresa(DeleteView, LoginRequiredMixin):
    model = Empresa
    success_url = reverse_lazy("inicio")