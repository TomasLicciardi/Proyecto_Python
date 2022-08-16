from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Mensaje(models.Model):
    titulo = models.CharField(max_length=40, default="Mensaje")
    emisor = models.ForeignKey(User, related_name="emisor", on_delete=models.CASCADE)
    receptor = models.ForeignKey(User, related_name="receptor", on_delete=models.CASCADE)
    contenido = models.CharField(max_length=1000)
    fecha = models.DateField(default=datetime.now)