from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Animales, Familiar,Vehiculos
from django.template import Template,Context,loader
from AppCoder.forms import FamiliarFormulario
from AppCoder.forms import AnimalFormulario
from AppCoder.forms import VehiculoFormulario

# Create your views here.

def familiar(self):

    familiar1 = Familiar(nombre="juan", edad="20",fechaDeNacimiento="2002-10-20")
    familiar1.save()
    
   
    familiar2 = Familiar(nombre="Maria", edad="40",fechaDeNacimiento="1982-07-13")
    familiar2.save()

    familiar3 = Familiar(nombre="Marcos", edad="30",fechaDeNacimiento="1992-08-20")
    familiar3.save()

    diccionario = {"nombre1":familiar1.nombre, "edad1":familiar1.edad,"fechaDeNacimiento1":familiar1.fechaDeNacimiento,"nombre2":familiar2.nombre, "edad2":familiar2.edad,"fechaDeNacimiento2":familiar2.fechaDeNacimiento,"nombre3":familiar3.nombre, "edad3":familiar3.edad,"fechaDeNacimiento3":familiar3.fechaDeNacimiento}
    
    nueva_plantilla= loader.get_template('template_entregable.html')


    documentoDeTexto = nueva_plantilla.render(diccionario)


    return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppCoder/inicio.html")

def animales(request):

      return render(request, "AppCoder/animales.html")

def vehiculos(request):

      return render(request, "AppCoder/vehiculos.html")

def familiarFormulario(request):
      if request.method == 'POST':

            miFormulario= FamiliarFormulario(request.POST)
            print(miFormulario)
            
            if miFormulario.is_valid:

                  informacion =miFormulario.cleaned_data
                  print(informacion)
                  familiar=Familiar(nombre=informacion['nombre'], edad=informacion['edad'],fechaDeNacimiento=informacion['fechaDeNacimiento'])

                  familiar.save()

                  return render(request, "AppCoder/inicio.html")

      else:

            miFormulario= FamiliarFormulario()

      return render(request, "AppCoder/familiarFormulario.html", {"miFormulario":miFormulario})

def animalFormulario(request):
      if request.method == 'POST':

            miFormulario= AnimalFormulario(request.POST)
            print(miFormulario)
            
            if miFormulario.is_valid:

                  informacion =miFormulario.cleaned_data
                  print(informacion)
                  animal=Animales(nombre=informacion['nombre'], fechaDeNacimiento=informacion['fechaDeNacimiento'],tipo=informacion['tipo'])

                  animal.save()

                  return render(request, "AppCoder/inicio.html")

      else:

            miFormulario= AnimalFormulario()

      return render(request, "AppCoder/animalFormulario.html", {"miFormulario":miFormulario})


def vehiculoFormulario(request):
      if request.method == 'POST':

            miFormulario= VehiculoFormulario(request.POST)
            print(miFormulario)
            
            if miFormulario.is_valid:

                  informacion =miFormulario.cleaned_data
                  print(informacion)
                  vehiculo=Vehiculos(kilometraje=informacion['kilometraje'], modelo=informacion['modelo'],tipo=informacion['tipo'])

                  vehiculo.save()

                  return render(request, "AppCoder/inicio.html")

      else:

            miFormulario= VehiculoFormulario()

      return render(request, "AppCoder/vehiculoFormulario.html", {"miFormulario":miFormulario})


def busquedaNombre(request):

      return render(request, "AppCoder/busquedaNombre.html")


def resultadosBusqueda(request):

      if request.GET['nombre']:
      #respuesta= f" ESTOY BUSCANDO AL FAMILIAR DE NOMBRE : {request.GET['nombre']}"
            nombre= request.GET['nombre']
            familiares=Familiar.objects.filter(nombre__icontains=nombre) 

            return render(request, "AppCoder/resultadosBusqueda.html",{"familiares":familiares,"nombre":nombre})

      else:
            respuesta= "No enviaste datos"

      return HttpResponse(respuesta)