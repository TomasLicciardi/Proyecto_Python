from pydoc import cli
from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def inicio(request):
    return render(request, "AppProyecto/index.html")

def empleados(request):
    if request.method == "POST":
        form = Empleado_form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            empleado = Empleado(nombre = info["nombre"], apellido = info["apellido"], salario = info["salario"], edad = info["edad"])
            empleado.save()
            return render(request, "AppProyecto/index.html")
    else:
        form = Empleado_form()
        return render(request, "AppProyecto/empleados.html", {"empleados_formulario": form})

def empresa(request):
    if request.method == "POST":
        form = Empresa_form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            empresa = Empresa(nombre = info["nombre"], direccion = info["direccion"])
            empresa.save()
            return render(request, "AppProyecto/index.html")
    else:
        form = Empresa_form()
        return render(request, "AppProyecto/empresa.html", {"empresa_formulario": form})

def clientes(request):
    if request.method == "POST":
        form = Cliente_form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            cliente = Cliente(nombre = info["nombre"], apellido = info["apellido"], direccion = info["direccion"], edad = info["edad"])
            cliente.save()
            return render(request, "AppProyecto/index.html")
    else:
        form = Cliente_form()
        return render(request, "AppProyecto/clientes.html", {"clientes_formulario": form})

def buscar_clientes(request):
    return render(request, "AppProyecto/busqueda_clientes.html")

def resultado_clientes(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        clientes = Cliente.objects.filter(nombre__icontains = nombre)
        return render(request, "AppProyecto/resultado_clientes.html", {"clientes": clientes})
    else:
        return render(request, "AppProyecto/busqueda_clientes.html", {"error": "No ha introducido nada en la busqueda!!"})
