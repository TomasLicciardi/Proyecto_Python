from django import forms

class MensajesForm(forms.Form):
    titulo = forms.CharField(max_length=40)
    emisor = forms.CharField(max_length=60)
    receptor = forms.CharField(max_length=60)
    contenido = forms.CharField(max_length=1000)
    fecha = forms.DateField()