from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import UpdateView, ListView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ListCliente(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "AppProyecto/list_clientes.html"

class CreateCliente(LoginRequiredMixin, CreateView):
    model = Cliente
    success_url = reverse_lazy("inicio")
    fields = ["nombre", "apellido", "direccion", "edad", "fecha", "imagen"]

class UpdateCliente(LoginRequiredMixin, UpdateView):
    model = Cliente
    success_url = reverse_lazy("inicio")
    fields = ["nombre", "apellido", "direccion", "edad","fecha", "imagen"]

class DeleteCliente(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy("inicio")

class ListEmpleado(LoginRequiredMixin, ListView):
    model = Empleado
    template_name = "AppProyecto/list_empleados.html"

class CreateEmpleado(LoginRequiredMixin, CreateView):
    model = Empleado
    success_url = reverse_lazy("inicio")
    fields = ["nombre", "apellido", "salario", "edad"]

class UpdateEmpleado(LoginRequiredMixin, UpdateView):
    model = Empleado
    success_url = reverse_lazy("inicio")
    fields = ["nombre", "apellido", "salario", "edad"]

class DeleteEmpleado(LoginRequiredMixin, DeleteView):
    model = Empleado
    success_url = reverse_lazy("inicio")

class ListEmpresa(LoginRequiredMixin, ListView):
    model = Empresa
    template_name = "AppProyecto/list_empresas.html"

class CreateEmpresa(LoginRequiredMixin, CreateView):
    model = Empresa
    success_url = reverse_lazy("inicio")
    fields = ["nombre", "direccion"]

class UpdateEmpresa(LoginRequiredMixin, UpdateView):
    model = Empresa
    success_url = reverse_lazy("inicio")
    fields = ["nombre", "direccion"]

class DeleteEmpresa(LoginRequiredMixin, DeleteView):
    model = Empresa
    success_url = reverse_lazy("inicio")