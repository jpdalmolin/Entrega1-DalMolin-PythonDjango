from socket import fromshare
from django import forms

class FamiliarFormulario(forms.Form):
    nombre=forms.CharField(max_length=20)
    edad=forms.IntegerField()
    fechaDeNacimiento=forms.DateField()


class AnimalFormulario(forms.Form):
    nombre=forms.CharField(max_length=20)
    fechaDeNacimiento=forms.DateField()
    tipo=forms.CharField(max_length=20)

class VehiculoFormulario(forms.Form):
    kilometraje=forms.IntegerField()
    modelo=forms.IntegerField()
    tipo=forms.CharField(max_length=20)