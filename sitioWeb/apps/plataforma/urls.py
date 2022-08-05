#Este archivo es para gestionar las rutas de la aplicacion plataforma

from django.conf import settings
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static


from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',login_required(views.home)),
    path('home/', login_required(views.home), name="homePage"),

    path('profesores/', login_required(views.profesores), name="profesoresPage"),
    path('registrarProfesor/', login_required(views.registrarProfesor)),
    path('edicionProfesor/<ident>', login_required(views.edicionProfesor)),
    path('editarProfesor/', login_required(views.editarProfesor)),
    path('eliminarProfesor/<ident>',login_required( views.eliminarProfesor)),

    path('acudientes/', login_required(views.acudientes)),
    path('registrarAcudiente/',login_required(views.registrarAcudiente)),
    path('edicionAcudiente/<ident>',login_required(views.edicionAcudiente)),
    path('editarAcudiente/', login_required(views.editarAcudiente)),
    path('eliminarAcudiente/<ident>', login_required(views.eliminarAcudiente)),

    path('cursos/', login_required(views.cursos)),
    path('registrarCurso/', login_required(views.registrarCurso)),
    path('edicionCurso/<ident>',login_required(views.edicionCurso)),
    path('editarCurso/', login_required(views.editarCurso)),
    # path('eliminarCurso/<ident>', login_required(views.eliminarCurso)),

    path('estudiantes/', login_required(views.estudiantes)),
    path('registrarEstudiante/', login_required(views.registrarEstudiante)),
    path('edicionEstudiante/<ident>',login_required(views.edicionEstudiante)),
    path('editarEstudiante/', login_required(views.editarEstudiante)),
    path('eliminarEstudiante/<ident>',login_required( views.eliminarEstudiante)),

    path('gestionEventos/', login_required(views.eventos)),
    path('registrarEvento/',login_required(views.registrarEvento)),
    path('edicionEvento/<ident>', login_required(views.edicionEvento)),
    path('editarEvento/', login_required(views.editarEvento)),
    path('eliminarEvento/<ident>', login_required(views.eliminarEvento)),

    path('asignaturas/', login_required(views.asignaturas)),
    path('registrarAsignatura/', login_required(views.registrarAsignatura)),
    path('edicionAsignatura/<ident>', login_required(views.edicionAsignatura)),
    path('editarAsignatura/', login_required(views.editarAsignatura)),
    path('eliminarAsignatura/<ident>', login_required(views.eliminarAsignatura)),

    path('notas/',login_required(views.notas)),
    path('registrarNota/', login_required(views.registrarNota)),
    path('verNotas/<ident>', login_required(views.verNotas), name='verNotasEstudiante'),
    path('edicionNota/<ident>', login_required(views.edicionNota)),
    path('editarNota/', login_required(views.editarNota)),
    path('eliminarNota/<ident>/<id_estudiante>', login_required(views.eliminarNota)),

    path('verNotasAcudiente/', login_required(views.verNotasAcudiente)),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
