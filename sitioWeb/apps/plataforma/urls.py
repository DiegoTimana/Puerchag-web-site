#Este archivo es para gestionar las rutas de la aplicacion plataforma

from msilib.schema import AdminExecuteSequence
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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

    path('eventos/', views.eventos)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)