from django import forms

class Cliente_form(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)
    edad = forms.IntegerField()


class Empleado_form(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    salario = forms.IntegerField()
    edad = forms.IntegerField()

class Empresa_form(forms.Form):
    nombre = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)