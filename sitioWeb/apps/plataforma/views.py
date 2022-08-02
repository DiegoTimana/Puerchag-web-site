from django.shortcuts import render, redirect
from .models import Evento, Profesor, Usuario, Curso, Estudiante, Acudiente

# Create your views here.

def home(request):
    return render(request, 'home.html',{})

def profesores(request):
    profesores = Usuario.objects.filter(es_profesor=True)
    return render(request,"gestionProfesor.html",{"profesores":profesores})



def registrarProfesor(request):

    ident = request.POST['numeroId']
    nombre = request.POST['txtNombre']
    apellido1 = request.POST['txtPrimerApellido']
    apellido2 = request.POST['txtSegundoApellido'] 
    email = request.POST['txtEmail']
    telefono = request.POST['txtTelefono']
    es_profesor = True
    password1 = request.POST['pwd']
    password2 = request.POST['pwd2']


    profesor = Usuario.objects.create(id=ident, username=nombre, primer_apellido=apellido1, segundo_apellido=apellido2,
    email=email,telefono_profesor=telefono, es_profesor = es_profesor, password=password1)

    return redirect('/profesores')

# def edicionProfesor(request, ident):
#     profesor = Usuario.objects.get(id_profesor=ident)
#     return render(request,"actualizarProfesor.html", {"profesor":profesor})

# def editarProfesor(request):
#     ident = request.POST['numeroId']
#     nombre = request.POST['txtNombre']
#     apellido1 = request.POST['txtPrimerApellido']
#     apellido2 = request.POST['txtSegundoApellido']
#     sexo = request.POST['Sexo']
#     email = request.POST['txtEmail']
#     telefono = request.POST['txtTelefono']
#     tipo_de_usuario = request.POST['Tipo']
#     estudio = request.POST['Estudio']
#     password = request.POST['pwd']
#     activo = request.POST['Activo']

#     profesor = Usuario.objects.get(id_profesor=ident)

#     profesor.id_profesor = ident
#     profesor.nombre = nombre
#     profesor.primer_apellido = apellido1
#     profesor.segundo_apellido = apellido2
#     profesor.sexo_profesor = sexo
#     profesor.email = email
#     profesor.telefono_profesor = telefono
#     profesor.tipo_de_usuario = tipo_de_usuario
#     profesor.nivel_estudios = estudio
#     profesor.password = password
#     profesor.vigencia = activo
#     profesor.save()
#     return redirect('/profesores')


# def borrarProfesor(request, ident):
#     profesor = Usuario.objects.get(id_profesor = ident)
#     profesor.delete()
#     return redirect('/profesores')

# def eliminarProfesor(request, ident):
#     profesor = Usuario.objects.get(id_profesor = ident)
#     profesor.vigencia = False
#     profesor.save()
#     return redirect('/profesores')


# #------------Acudiente----------------------------------------------------

# # def acudientes(request):
# #     acudientes = Acudiente.objects.all()
# #     return render(request,"gestionAcudiente.html",{"acudientes":acudientes})

# # def registrarAcudiente(request):

# #     ident = request.POST['numeroId']
# #     # nombre = request.POST['txtNombre']
# #     # apellido1 = request.POST['txtPrimerApellido']
# #     # apellido2 = request.POST['txtSegundoApellido']
# #     # email = request.POST['txtEmail']
# #     # telefono = request.POST['txtTelefono']
# #     # password = request.POST['pwd']
# #     # activo = request.POST['Activo']

# #     acudiente = Acudiente.objects.create(id_acudiente=ident, usuario= Usuario.objects.get(id_profesor=idProfesor))

# #     return redirect('/acudientes')


# # def edicionAcudiente(request, ident):
# #     acudiente = Acudiente.objects.get(id_acudiente=ident)
# #     return render(request,"actualizarAcudiente.html", {"acudiente":acudiente})

# # def editarAcudiente(request):
# #     ident = request.POST['numeroId']
# #     nombre = request.POST['txtNombre']
# #     apellido1 = request.POST['txtPrimerApellido']
# #     apellido2 = request.POST['txtSegundoApellido']
# #     email = request.POST['txtEmail']
# #     telefono = request.POST['txtTelefono']
# #     password = request.POST['pwd']
# #     activo = request.POST['Activo']

# #     acudiente = Acudiente.objects.get(id_acudiente=ident)

# #     acudiente.id_acudiente = ident
# #     acudiente.nombre = nombre
# #     acudiente.primer_apellido = apellido1
# #     acudiente.segundo_apellido = apellido2
# #     acudiente.email = email
# #     acudiente.telefono = telefono
# #     acudiente.password = password
# #     acudiente.vigencia = activo
# #     acudiente.save()
# #     return redirect('/acudientes')


# # def borrarAcudiente(request, ident):
# #     acudiente = Acudiente.objects.get(id_acudiente = ident)
# #     acudiente.delete()
# #     return redirect('/acudientes')

# # def eliminarAcudiente(request, ident):
# #     acudiente = Acudiente.objects.get(id_acudiente = ident)
# #     acudiente.vigencia = False
# #     acudiente.save()
# #     return redirect('/acudientes')

# #--------------Cursos------------------

# def cursos(request):
#     cursos = Curso.objects.all()
#     profesores = Usuario.objects.all()
#     return render(request,"gestionCurso.html",{"cursos":cursos, "profesores":profesores})


# def registrarCurso(request):

#     ident = request.POST['numeroId']
#     nombre = request.POST['txtNombre']
#     periodo = request.POST['txtPeriodoElectivo']
#     idProfesor = request.POST['numeroIdProfesor']


#     curso = Curso.objects.create(id_curso=ident, nombre=nombre, periodo_electivo=periodo, id_profesor= Usuario.objects.get(id_profesor=idProfesor))

#     return redirect('/cursos')

# def edicionCurso(request, ident):
#     curso = Curso.objects.get(id_curso=ident)
#     profesores = Usuario.objects.all()
#     return render(request,"actualizarCurso.html", {"curso":curso,"profesores":profesores})

# def editarCurso(request):
#     ident = request.POST['numeroId']
#     nombre = request.POST['txtNombre']
#     periodo = request.POST['txtPeriodoElectivo']
#     idProfesor = request.POST['numeroIdProfesor']

#     curso = Curso.objects.get(id_curso=ident)

#     curso.id_curso = ident
#     curso.nombre = nombre
#     curso.periodo_electivo = periodo
#     curso.id_profesor = Usuario.objects.get(id_profesor=idProfesor)

#     curso.save()
#     return redirect('/cursos')

# def eliminarCurso(request, ident):
#     curso = Curso.objects.get(id_curso = ident)
#     curso.delete()
#     return redirect('/cursos')

# #----------estudiante-------------------------------------

# def estudiantes(request):
#     estudiantes = Estudiante.objects.all()
#     cursos =  Curso.objects.all()
#     acudientes = Usuario.objects.all()
#     return render(request,"gestionEstudiante.html",{"estudiantes":estudiantes,"cursos":cursos,"acudientes":acudientes})

# def registrarEstudiante(request):

#     ident = request.POST['numeroId']
#     nombre = request.POST['txtNombre']
#     apellido1 = request.POST['txtPrimerApellido']
#     apellido2 = request.POST['txtSegundoApellido']
#     fechaNacimiento = request.POST['fechaNacimiento']
#     sexo = request.POST['Sexo']
#     curso = request.POST['numeroIdCurso']
#     acudiente = request.POST['numeroIdAcudiente']
#     activo = request.POST['Activo']

#     estudiante = Estudiante.objects.create(id_estudiante=ident, nombre=nombre, primer_apellido=apellido1, segundo_apellido=apellido2, fecha_nacimiento=fechaNacimiento,
#     sexo = sexo, id_curso=Curso.objects.get(id_curso=curso), id_acudiente=Usuario.objects.get(id_profesor=acudiente), vigencia=activo)

#     return redirect('/estudiantes')

# def edicionEstudiante(request, ident):
#     estudiante = Estudiante.objects.get(id_estudiante=ident)
#     cursos =  Curso.objects.all()
#     acudientes = Usuario.objects.all()
#     return render(request,"actualizarEstudiante.html", {"estudiante":estudiante,"cursos":cursos,"acudientes":acudientes})

# def editarEstudiante(request):
#     ident = request.POST['numeroId']
#     nombre = request.POST['txtNombre']
#     apellido1 = request.POST['txtPrimerApellido']
#     apellido2 = request.POST['txtSegundoApellido']
#     fechaNacimiento = request.POST['fechaNacimiento']
#     sexo = request.POST['Sexo']
#     curso = request.POST['numeroIdCurso']
#     acudiente = request.POST['numeroIdAcudiente']
#     activo = request.POST['Activo']

#     estudiante = Estudiante.objects.get(id_estudiante=ident)

#     estudiante.id_estudiante=ident 
#     estudiante.nombre=nombre 
#     estudiante.primer_apellido=apellido1
#     estudiante.segundo_apellido=apellido2
#     estudiante.fecha_nacimiento=fechaNacimiento
#     estudiante.sexo = sexo
#     estudiante.id_curso=Curso.objects.get(id_curso=curso)
#     estudiante.id_acudiente=Usuario.objects.get(id_profesor=acudiente)
#     estudiante.vigencia=activo
#     estudiante.save()
#     return redirect('/estudiantes')

# def eliminarEstudiante(request, ident):
#     estudiante = Estudiante.objects.get(id_estudiante = ident)
#     estudiante.vigencia = False
#     estudiante.save()
#     return redirect('/estudiantes')
