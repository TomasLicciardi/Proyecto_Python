from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(request, "AppProyecto/index.html")