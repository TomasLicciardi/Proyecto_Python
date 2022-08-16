from AppMensajeria.models import *
from AppMensajeria.forms import *
from django.views.generic import ListView , CreateView, DeleteView , DetailView
from django.urls import reverse_lazy

# Django authentication

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class MensajeList(LoginRequiredMixin, ListView):

    model = Mensaje
    template_name = "AppMensajeria/mensaje_list.html"

class MensajeDetail(LoginRequiredMixin, DetailView):

    model = Mensaje
    template_name = "AppMensajeria/mensaje_detail.html"

class MensajeCreate(LoginRequiredMixin, CreateView):

    model = Mensaje
    success_url = reverse_lazy("mensajes")
    fields = ['titulo','emisor', 'receptor', 'contenido', 'fecha']


class MensajeDelete(LoginRequiredMixin, DeleteView):

    model = Mensaje
    success_url = reverse_lazy("mensajes")