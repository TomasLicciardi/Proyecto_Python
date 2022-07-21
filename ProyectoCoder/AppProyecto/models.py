from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre + " " + self.apellido

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    salario = models.IntegerField()
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre + " " + self.apellido


class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
