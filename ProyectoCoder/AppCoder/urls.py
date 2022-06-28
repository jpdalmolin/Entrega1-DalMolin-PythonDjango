from django.urls import path

from AppCoder import views

urlpatterns = [
   
    path('inicio', views.inicio, name="inicio"), #esta era nuestra primer view
    path('familiar', views.familiar, name="familiar"),
    path('animales', views.animales, name="animales"),
    path('vehiculos', views.vehiculos, name="vehiculos"),
    path('familiarFormulario', views.familiarFormulario, name="familiarFormulario"),
    path('animalFormulario', views.animalFormulario, name="animalFormulario"),
    path('vehiculoFormulario', views.vehiculoFormulario, name="vehiculoFormulario"),
    path('busquedaNombre', views.busquedaNombre, name="busquedaNombre"),
    path('resultadosBusqueda', views.resultadosBusqueda, name="resultadosBusqueda"),
]

