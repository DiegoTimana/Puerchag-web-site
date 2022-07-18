#Este archivo es para gestionar las rutas de la aplicacion plataforma

from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('home/', views.home, name="homePage"),
    path('profesores/', views.profesores, name="profesoresPage"),
    path('registrarProfesor/', views.registrarProfesor),
    path('edicionProfesor/<ident>', views.edicionProfesor),
    path('editarProfesor/', views.editarProfesor),
    path('eliminarProfesor/<ident>', views.eliminarProfesor)
]