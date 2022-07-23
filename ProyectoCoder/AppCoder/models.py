from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Familiar(models.Model):
    nombre=models.CharField(max_length=20)
    edad=models.IntegerField()
    fechaDeNacimiento=models.DateField()
    def __str__(self):
            return f"Nombre:{self.nombre} - Edad {self.edad} - Nacimiento {self.fechaDeNacimiento}"

class Animales(models.Model):
    nombre=models.CharField(max_length=20)
    fechaDeNacimiento=models.DateField()
    tipo=models.CharField(max_length=20)
    def __str__(self):
            return f"Nombre:{self.nombre} - Nacimiento {self.fechaDeNacimiento} - tipo {self.tipo}"

class Vehiculos(models.Model):
    kilometraje=models.IntegerField()
    modelo=models.IntegerField()
    tipo=models.CharField(max_length=20)
    def __str__(self):
            return f"Kilometraje:{self.kilometraje} - Modelo {self.modelo} - tipo {self.tipo}"
        

class Avatar(models.Model):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    imagen=models.ImageField(upload_to='avatares', null=True, blank=True)