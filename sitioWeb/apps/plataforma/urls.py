#Este archivo es para gestionar las rutas de la aplicacion plataforma

from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('',login_required(views.home)),
    path('home/', login_required(views.home), name="homePage"),

    path('profesores/', login_required(views.profesores), name="profesoresPage"),
    path('registrarProfesor/', login_required(views.registrarProfesor)),
    path('edicionProfesor/<ident>', login_required(views.edicionProfesor)),
    path('editarProfesor/', login_required(views.editarProfesor)),
    # path('eliminarProfesor/<ident>',login_required( views.eliminarProfesor)),

    # # path('acudientes/', login_required(views.acudientes)),
    # # path('registrarAcudiente/',login_required(views.registrarAcudiente)),
    # # path('edicionAcudiente/<ident>',login_required(views.edicionAcudiente)),
    # # path('editarAcudiente/', login_required(views.editarAcudiente)),
    # # path('eliminarAcudiente/<ident>', login_required(views.eliminarAcudiente)),

    # path('cursos/', login_required(views.cursos)),
    # path('registrarCurso/', login_required(views.registrarCurso)),
    # path('edicionCurso/<ident>',login_required(views.edicionCurso)),
    # path('editarCurso/', login_required(views.editarCurso)),
    # path('eliminarCurso/<ident>', login_required(views.eliminarCurso)),

    # path('estudiantes/', login_required(views.estudiantes)),
    # path('registrarEstudiante/', login_required(views.registrarEstudiante)),
    # path('edicionEstudiante/<ident>',login_required(views.edicionEstudiante)),
    # path('editarEstudiante/', login_required(views.editarEstudiante)),
    # path('eliminarEstudiante/<ident>',login_required( views.eliminarEstudiante)),

]