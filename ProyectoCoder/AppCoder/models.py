from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre=models.CharField(max_length=20)
    edad=models.IntegerField()
    fechaDeNacimiento=models.DateField()

class Animales(models.Model):
    nombre=models.CharField(max_length=20)
    fechaDeNacimiento=models.DateField()
    tipo=models.CharField(max_length=20)

class Vehiculos(models.Model):
    kilometraje=models.IntegerField()
    modelo=models.IntegerField()
    tipo=models.CharField(max_length=20)