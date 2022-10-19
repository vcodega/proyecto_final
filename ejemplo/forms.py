from django import forms

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100) #interaccion con el usuario