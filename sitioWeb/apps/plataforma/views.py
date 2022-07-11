from django.shortcuts import render, redirect
from .models import Profesor

# Create your views here.

def home(request):
    return render(request, 'home.html',{})

def profesores(request):
    profesores = Profesor.objects.all()
    return render(request,"gestionProfesor.html",{"profesores":profesores})



def registrarProfesor(request):

    ident = request.POST['numeroId']
    nombre = request.POST['txtNombre']
    apellido1 = request.POST['txtPrimerApellido']
    apellido2 = request.POST['txtSegundoApellido']
    sexo = request.POST['Sexo']
    email = request.POST['txtEmail']
    telefono = request.POST['txtTelefono']
    cargo = request.POST['Cargo']
    estudio = request.POST['Estudio']
    password = request.POST['pwd']
    activo = request.POST['Activo']

    profesor = Profesor.objects.create(id_profesor=ident, nombre=nombre, primer_apellido=apellido1, segundo_apellido=apellido2,
    sexo_profesor = sexo, email_profesor=email ,telefono_profesor=telefono, cargo=cargo, nivel_estudios=estudio, password=password, vigencia=activo)

    return redirect('/profesores')

def edicionProfesor(request, ident):
    profesor = Profesor.objects.get(id_profesor=ident)
    return render(request,"actualizarProfesor.html", {"profesor":profesor})

def editarProfesor(request):
    ident = request.POST['numeroId']
    nombre = request.POST['txtNombre']
    apellido1 = request.POST['txtPrimerApellido']
    apellido2 = request.POST['txtSegundoApellido']
    sexo = request.POST['Sexo']
    email = request.POST['txtEmail']
    telefono = request.POST['txtTelefono']
    cargo = request.POST['Cargo']
    estudio = request.POST['Estudio']
    password = request.POST['pwd']
    activo = request.POST['Activo']

    profesor = Profesor.objects.get(id_profesor=ident)

    profesor.id_profesor = ident
    profesor.nombre = nombre
    profesor.primer_apellido = apellido1
    profesor.segundo_apellido = apellido2
    profesor.sexo_profesor = sexo
    profesor.email_profesor = email
    profesor.telefono_profesor = telefono
    profesor.cargo = cargo
    profesor.nivel_estudios = estudio
    profesor.password = password
    profesor.vigencia = activo
    profesor.save()
    return redirect('/profesores')


def eliminarProfesor(request, ident):
    profesor = Profesor.objects.get(id_profesor = ident)
    profesor.delete()
    return redirect('/profesores')
