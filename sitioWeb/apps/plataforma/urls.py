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
    path('eliminarProfesor/<ident>', views.eliminarProfesor),

    path('acudientes/', views.acudientes),
    path('registrarAcudiente/',views.registrarAcudiente),
    path('edicionAcudiente/<ident>',views.edicionAcudiente),
    path('editarAcudiente/', views.editarAcudiente),
    path('eliminarAcudiente/<ident>', views.eliminarAcudiente),

    path('cursos/', views.cursos),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<ident>',views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<ident>', views.eliminarCurso),

    path('estudiantes/', views.estudiantes),
    path('registrarEstudiante/', views.registrarEstudiante),
    path('edicionEstudiante/<ident>',views.edicionEstudiante),
    path('editarEstudiante/', views.editarEstudiante),
    path('eliminarEstudiante/<ident>', views.eliminarEstudiante),

]