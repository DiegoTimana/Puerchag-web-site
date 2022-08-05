from django.shortcuts import render, redirect
from .models import Profesor, Acudiente, Curso, Estudiante, Asignatura, Nota, Usuario, Evento

# Create your views here.

def home(request):
    esProfesor = request.user.es_profesor
    esAcudiente = request.user.es_acudiente
    esAdmin = request.user.es_administrador

    return render(request, 'home.html',{"esProfesor":esProfesor, "esAcudiente":esAcudiente, "esAdmin":esAdmin})

def profesores(request):
    esProfesor = request.user.es_profesor
    esAcudiente = request.user.es_acudiente
    esAdmin = request.user.es_administrador
    
    profesores = Usuario.objects.filter(es_profesor=True, vigencia=True).order_by('id')

    return render(request,"gestionProfesor.html",{"profesores":profesores, "esProfesor":esProfesor, "esAcudiente":esAcudiente, "esAdmin":esAdmin})

def registrarProfesor(request):
    ident = request.POST['numeroId']
    nombre = request.POST['txtNombre']
    apellido1 = request.POST['txtPrimerApellido']
    apellido2 = request.POST['txtSegundoApellido']
    email = request.POST['txtEmail']
    telefono = request.POST['txtTelefono'] 
    password = request.POST['pwd']
 
    profesor = Usuario.objects.create_user(id=ident, username=nombre, primer_apellido=apellido1, segundo_apellido=apellido2,
    email=email ,telefono_profesor=telefono, es_profesor=True, es_acudiente=False, es_administrador=False, password=password)

    return redirect('/profesores')

def edicionProfesor(request, ident):
    esProfesor = request.user.es_profesor
    esAcudiente = request.user.es_acudiente
    esAdmin = request.user.es_administrador

    profesor = Usuario.objects.get(id=ident)
    return render(request,"actualizarProfesor.html", {"profesor":profesor, "esProfesor":esProfesor, "esAcudiente":esAcudiente, "esAdmin":esAdmin})

def editarProfesor(request):
    ident = request.POST['numeroId']
    nombre = request.POST['txtNombre']
    apellido1 = request.POST['txtPrimerApellido']
    apellido2 = request.POST['txtSegundoApellido']
    email = request.POST['txtEmail']
    telefono = request.POST['txtTelefono']
    password = request.POST['pwd']
    activo = request.POST['Activo']

    profesor = Usuario.objects.get(id=ident)

    profesor.id = ident
    profesor.nombre = nombre
    profesor.primer_apellido = apellido1
    profesor.segundo_apellido = apellido2
    profesor.email_profesor = email
    profesor.telefono_profesor = telefono
    profesor.password = password
    profesor.vigencia = activo
    profesor.save()
    return redirect('/profesores')

def eliminarProfesor(request, ident):
    profesor = Usuario.objects.get(id = ident)
    profesor.vigencia = False
    profesor.save()
    return redirect('/profesores')

#------------Acudiente----------------------------------------------------

def acudientes(request):
    esProfesor = request.user.es_profesor
    esAcudiente = request.user.es_acudiente
    esAdmin = request.user.es_administrador

    acudientes = Usuario.objects.filter(es_acudiente=True).order_by('id')
    return render(request,"gestionAcudiente.html",{"acudientes":acudientes, "esProfesor":esProfesor, "esAcudiente":esAcudiente, "esAdmin":esAdmin})

def registrarAcudiente(request):
    ident = request.POST['numeroId']
    nombre = request.POST['txtNombre']
    apellido1 = request.POST['txtPrimerApellido']
    apellido2 = request.POST['txtSegundoApellido']
    email = request.POST['txtEmail']
    telefono = request.POST['txtTelefono']
    password = request.POST['pwd']

    acudiente = Usuario.objects.create_user(id=ident, username=nombre, primer_apellido=apellido1, segundo_apellido=apellido2,
    email=email ,telefono_profesor=telefono, es_profesor=False, es_acudiente=True, es_administrador=False, password=password)

    return redirect('/acudientes')

def edicionAcudiente(request, ident):
    esProfesor = request.user.es_profesor
    esAcudiente = request.user.es_acudiente
    esAdmin = request.user.es_administrador

    acudiente = Usuario.objects.get(id=ident)
    return render(request,"actualizarAcudiente.html", {"acudiente":acudiente, "esProfesor":esProfesor, "esAcudiente":esAcudiente, "esAdmin":esAdmin})

def editarAcudiente(request):
    ident = request.POST['numeroId']
    nombre = request.POST['txtNombre']
    apellido1 = request.POST['txtPrimerApellido']
    apellido2 = request.POST['txtSegundoApellido']
    email = request.POST['txtEmail']
    telefono = request.POST['txtTelefono']
    password = request.POST['pwd']
    activo = request.POST['Activo']

    acudiente = Usuario.objects.get(id=ident)

    acudiente.id = ident
    acudiente.nombre = nombre
    acudiente.primer_apellido = apellido1
    acudiente.segundo_apellido = apellido2
    acudiente.email = email
    acudiente.telefono_profesor = telefono
    acudiente.password = password
    acudiente.vigencia = activo
    acudiente.save()
    return redirect('/acudientes')

def eliminarAcudiente(request, ident):
    acudiente = Usuario.objects.get(id = ident)
    acudiente.vigencia = False
    acudiente.save()
    return redirect('/acudientes')

#--------------Cursos------------------

def cursos(request):
    esProfesor = request.user.es_profesor
    esAcudiente = request.user.es_acudiente
    esAdmin = request.user.es_administrador

    cursos = Curso.objects.all()
    profesores = Usuario.objects.filter(es_profesor=True, vigencia=True)
    cursos1 = Curso.objects.select_related('id_profesor')
    return render(request,"gestionCurso.html",{"cursos1":cursos1, "profesores":profesores, "esProfesor":esProfesor, "esAcudiente":esAcudiente, "esAdmin":esAdmin})

def registrarCurso(request):
    ident = request.POST['numeroId']
    nombre = request.POST['txtNombre']
    periodo = request.POST['txtPeriodoElectivo']
    idProfesor = request.POST['numeroIdProfesor']

    curso = Curso.objects.create(id_curso=ident, nombre=nombre, periodo_electivo=periodo, id_profesor=Usuario.objects.get(id=idProfesor))
    return redirect('/cursos')

def edicionCurso(request, ident):
    esProfesor = request.user.es_profesor
    esAcudiente = request.user.es_acudiente
    esAdmin = request.user.es_administrador

    curso = Curso.objects.get(id_curso=ident)
    profesores = Usuario.objects.filter(es_profesor=True)
    return render(request,"actualizarCurso.html", {"curso":curso,"profesores":profesores, "esProfesor":esProfesor, "esAcudiente":esAcudiente, "esAdmin":esAdmin})

def editarCurso(request):
    ident = request.POST['numeroId']
    nombre = request.POST['txtNombre']
    periodo = request.POST['txtPeriodoElectivo']
    idProfesor = request.POST['numeroIdProfesor']

    curso = Curso.objects.get(id_curso=ident)

    curso.id_acudiente = ident
    curso.nombre = nombre
    curso.periodo_electivo = periodo
    curso.id_profesor = Usuario.objects.get(id=idProfesor)
    curso.save()
    return redirect('/cursos')

def eliminarCurso(request, ident):
    curso = Curso.objects.get(id_curso = ident)
    curso.delete()
    return redirect('/cursos')

#----------estudiante-------------------------------------

def estudiantes(request):
    esProfesor = request.user.es_profesor
    esAcudiente = request.user.es_acudiente
    esAdmin = request.user.es_administrador

    cursos =  Curso.objects.all()
    estudiantes = Estudiante.objects.select_related('id_curso')
    acudientes = Usuario.objects.filter(es_acudiente=True, vigencia=True).order_by('id')
    return render(request,"gestionEstudiante.html",{"estudiantes":estudiantes,"cursos":cursos,"acudientes":acudientes, "esProfesor":esProfesor, "esAcudiente":esAcudiente, "esAdmin":esAdmin})

def registrarEstudiante(request):

    ident = request.POST['numeroId']
    nombre = request.POST['txtNombre']
    apellido1 = request.POST['txtPrimerApellido']
    apellido2 = request.POST['txtSegundoApellido']
    fechaNacimiento = request.POST['fechaNacimiento']
    sexo = request.POST['Sexo']
    curso = request.POST['numeroIdCurso']
    acudiente = request.POST['numeroIdAcudiente']

    estudiante = Estudiante.objects.create(id_estudiante=ident, nombre=nombre, primer_apellido=apellido1, segundo_apellido=apellido2, fecha_nacimiento=fechaNacimiento,
    sexo = sexo, id_curso=Curso.objects.get(id_curso=curso), id_acudiente=Usuario.objects.get(id=acudiente), vigencia=True)
    return redirect('/estudiantes')

def edicionEstudiante(request, ident):
    esProfesor = request.user.es_profesor
    esAcudiente = request.user.es_acudiente
    esAdmin = request.user.es_administrador

    estudiante = Estudiante.objects.get(id_estudiante=ident)
    cursos =  Curso.objects.all()
    acudientes = Usuario.objects.filter(es_acudiente=True).order_by('id')
    return render(request,"actualizarEstudiante.html", {"estudiante":estudiante,"cursos":cursos,"acudientes":acudientes, "esProfesor":esProfesor, "esAcudiente":esAcudiente, "esAdmin":esAdmin})

def editarEstudiante(request):
    ident = request.POST['numeroId']
    nombre = request.POST['txtNombre']
    apellido1 = request.POST['txtPrimerApellido']
    apellido2 = request.POST['txtSegundoApellido']
    fechaNacimiento = request.POST['fechaNacimiento']
    sexo = request.POST['Sexo']
    curso = request.POST['numeroIdCurso']
    acudiente = request.POST['numeroIdAcudiente']
    activo = request.POST['Activo']

    estudiante = Estudiante.objects.get(id_estudiante=ident)

    estudiante.id_estudiante=ident 
    estudiante.nombre=nombre 
    estudiante.primer_apellido=apellido1
    estudiante.segundo_apellido=apellido2
    estudiante.fecha_nacimiento=fechaNacimiento
    estudiante.sexo = sexo
    estudiante.id_curso=Curso.objects.get(id_curso=curso)
    estudiante.id_acudiente=Usuario.objects.get(id=acudiente)
    estudiante.vigencia=activo
    estudiante.save()
    return redirect('/estudiantes')

def eliminarEstudiante(request, ident):
    estudiante = Estudiante.objects.get(id_estudiante = ident)
    estudiante.vigencia = False
    estudiante.save()
    return redirect('/estudiantes')

#-------------------------------------asignatura---------------------------------------------------

def asignaturas(request):
    esProfesor = request.user.es_profesor
    esAcudiente = request.user.es_acudiente
    esAdmin = request.user.es_administrador

    cursos =  Curso.objects.all()
    asignaturas = Asignatura.objects.select_related('id_curso').order_by('id_asignatura')
    return render(request,"gestionAsignatura.html",{"asignaturas":asignaturas,"cursos":cursos, "esProfesor":esProfesor, "esAcudiente":esAcudiente, "esAdmin":esAdmin})

def registrarAsignatura(request):
    ident = request.POST['numeroId']
    nombre = request.POST['txtNombre']
    curso = request.POST['numeroIdCurso']

    asignatura = Asignatura.objects.create(id_asignatura=ident, nombre=nombre, id_curso=Curso.objects.get(id_curso=curso))
    return redirect('/asignaturas')


def edicionAsignatura(request, ident):
    esProfesor = request.user.es_profesor
    esAcudiente = request.user.es_acudiente
    esAdmin = request.user.es_administrador

    asignatura = Asignatura.objects.get(id_asignatura=ident)
    cursos =  Curso.objects.all()
    return render(request,"actualizarAsignatura.html", {"asignatura":asignatura,"cursos":cursos, "esProfesor":esProfesor, "esAcudiente":esAcudiente, "esAdmin":esAdmin})

def editarAsignatura(request):
    ident = request.POST['numeroId']
    nombre = request.POST['txtNombre']
    curso = request.POST['numeroIdCurso']

    asignatura = Asignatura.objects.get(id_asignatura=ident)

    asignatura.id_asignatura=ident 
    asignatura.nombre=nombre 
    asignatura.id_curso=Curso.objects.get(id_curso=curso)
    asignatura.save()
    return redirect('/asignaturas')

def eliminarAsignatura(request, ident):
    asignatura = Asignatura.objects.get(id_asignatura = ident)
    asignatura.delete()
    return redirect('/asignaturas')




#--------------------------------Notas---------------------------------------------

def notas(request):
    esProfesor = request.user.es_profesor
    esAcudiente = request.user.es_acudiente
    esAdmin = request.user.es_administrador

    idUser = request.user.id
    idProfesor = Usuario.objects.get(id=idUser)
    curso = Curso.objects.get(id_profesor=idProfesor)

    cursos = Curso.objects.all()
    asignaturas = Asignatura.objects.filter(id_curso = curso).order_by('id_asignatura')
    estudiantes = Estudiante.objects.filter(id_curso = curso).order_by('primer_apellido')
    return render(request,"gestionNota.html",{"cursos":cursos, "asignaturas":asignaturas, "estudiantes":estudiantes, "esProfesor":esProfesor, "esAcudiente":esAcudiente, "esAdmin":esAdmin})

def registrarNota(request):
    ident = request.POST['numeroId']
    calificacion = request.POST['numeroCalificacion']
    periodo = request.POST['txtPeriodo']
    fecha = request.POST['fechaNota']
    titulo = request.POST['txtTitulo']
    comentario = request.POST['txtComentario']
    id_asignatura = request.POST['numeroIdAsignatura']
    id_estudiante = request.POST['numeroIdEstudiante']

    nota = Nota.objects.create(id_nota=ident, calificacion=calificacion, periodo= periodo, fecha=fecha, titulo=titulo, comentario=comentario,
        id_asignatura=Asignatura.objects.get(id_asignatura=id_asignatura), id_estudiante=Estudiante.objects.get(id_estudiante=id_estudiante))

    return redirect('/notas')

def verNotas(request, ident):
    esProfesor = request.user.es_profesor
    esAcudiente = request.user.es_acudiente
    esAdmin = request.user.es_administrador

    asignaturas = Asignatura.objects.all()
    estudiante = Estudiante.objects.select_related('id_curso').get(id_estudiante=ident)

    notas = Nota.objects.select_related('id_asignatura').filter(id_estudiante=ident).order_by('id_asignatura')
    return render(request,"verNotas.html",{"notas":notas, "estudiante":estudiante, "esProfesor":esProfesor, "esAcudiente":esAcudiente, "esAdmin":esAdmin})

def edicionNota(request, ident):
    esProfesor = request.user.es_profesor
    esAcudiente = request.user.es_acudiente
    esAdmin = request.user.es_administrador

    nota = Nota.objects.get(id_nota=ident)
    return render(request,"actualizarNota.html",{"nota":nota, "esProfesor":esProfesor, "esAcudiente":esAcudiente, "esAdmin":esAdmin})

def editarNota(request):
    ident = request.POST['numeroId']
    calificacion = request.POST['numeroCalificacion']
    periodo = request.POST['txtPeriodo']
    fecha = request.POST['fechaNota']
    titulo = request.POST['txtTitulo']
    comentario = request.POST['txtComentario']
    id_asignatura = request.POST['numeroIdAsignatura']
    id_estudiante = request.POST['numeroIdEstudiante']

    nota = Nota.objects.get(id_nota= ident)

    nota.id_nota = ident
    nota.calificacion = calificacion
    nota.periodo = periodo
    nota.fecha = fecha
    nota.titulo = titulo
    nota.comentario = comentario
    nota.id_asignatura = Asignatura.objects.get(id_asignatura=id_asignatura)
    nota.id_estudiante = Estudiante.objects.get(id_estudiante=id_estudiante) 
    nota.save()
    return redirect('verNotasEstudiante', id_estudiante)

def eliminarNota(request, ident, id_estudiante):
    nota = Nota.objects.get(id_nota = ident)
    nota.delete()
    return redirect('verNotasEstudiante', id_estudiante)   

def eventos(request):
    esProfesor = request.user.es_profesor
    esAcudiente = request.user.es_acudiente
    esAdmin = request.user.es_administrador

    eventos = Evento.objects.all()
    return render(request,"gestionEventos.html",{"eventos":eventos, "esProfesor":esProfesor, "esAcudiente":esAcudiente, "esAdmin":esAdmin})

def registrarEvento(request):

    id = request.POST['numeroId']
    Fecha = request.POST['fecha']
    Hora = request.POST['hora']
    detalles = request.POST['detalle']
    imagen = request.FILES['imagen']
    evento = Evento.objects.create(id_evento=id, fecha=Fecha, hora=Hora, detalle= detalles, imagen=imagen)
    return redirect('/gestionEventos')

def editarEvento(request):

    id = request.POST['numeroId']
    Fecha = request.POST['fecha']
    Hora = request.POST['hora']
    detalles = request.POST['detalle']
    imagen = request.FILES['imagen']
    evento = Evento.objects.create(id_evento=id, fecha=Fecha, hora=Hora, detalle= detalles, imagen=imagen)
    return redirect('/gestionEventos')

#------------Notas Para Acudientes----------------------------

def verNotasAcudiente(request):
    esProfesor = request.user.es_profesor
    esAcudiente = request.user.es_acudiente
    esAdmin = request.user.es_administrador

    numeroId = request.user.id
    idAcudiente = Usuario.objects.get(id=numeroId)

    asignaturas = Asignatura.objects.all()


    estudiante = Estudiante.objects.select_related('id_curso').get(id_acudiente=idAcudiente)

    notas = Nota.objects.select_related('id_asignatura').filter(id_estudiante=estudiante).order_by('id_asignatura')

    return render(request,"verNotasAcudiente.html",{"notas":notas, "estudiante":estudiante, "esProfesor":esProfesor, "esAcudiente":esAcudiente, "esAdmin":esAdmin})

