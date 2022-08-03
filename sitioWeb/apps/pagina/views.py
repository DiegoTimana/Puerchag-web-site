import json
from multiprocessing import AuthenticationError
from telnetlib import AUTHENTICATION
from django.conf import settings
from django.shortcuts import redirect, render
from django.core.mail import send_mail
import urllib
from django.contrib import messages
import urllib3


# Create your views here.
#Para crear una vista, definir la funcion en la parte de abajo, cambiar el nombre y el path. Luego agregar la url al archivo
#urls.py. Por último verificar que el archivo html funcione correctamente (que los archivos estaticos tenga las etiquetas, 
# ej. archivos css y javascript, y que las imagenes tengan la ruta correcta, ej agregar /static a la ruta)

#vista del indexx
def index(request): 
    return render(request, "pagina/index.html")

#vista del login FALTA VALIDAR EL CAPTCHA, NO SE COMOOOO
def login(request):
    if request.method == 'POST':
            print("hola")
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.urlencode(values)
            req = urllib3.Request(url, data)
            response = urllib3.urlopen(req)
            result = json.load(response)
            ''' End reCAPTCHA validation '''
            if result['success']:
                messages.success(request, 'PASO CAPTCHA')
            else:
                messages.error(request, 'Invalid reCAPTCHA. INTENTE NUEVAMENTE.')

            return redirect('accounts/login/')
    else:
        return render(request, 'accounts/login/')


#vista de contactanos (enviar e-mail)
def contact(request): 
    return render(request, "pagina/contact.html")

#recibir datos del formulario de contacto y enviar e-mail  
def contactar(request): 
    if request.method == "POST":
        asunto = request.POST["subject"]
        mensaje = request.POST["message"] + "\n" + "\nContacto" + "\nNombre: " + request.POST["name"] + "\nCorreo: " + request.POST["email"] + "\nNúmero: " + request.POST["number"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["alexistimana021@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently = False)
        return render(request, "pagina/login.html")
    else: 
        return render(request, "pagina/contact.html")

#vista de profesores
def teachers(request): 
    return render(request, "pagina/teachers.html")

#vista del single
def single(request): 
    return render(request, "pagina/single.html")

#vista del single-sidebar
def singleSidebar(request): 
    return render(request, "pagina/single-sidebar.html")

#vista de event-list
def eventList(request): 
    return render(request, "pagina/event-list.html")

#vista de galeria
def galeria(request): 
    return render(request, "pagina/gallery-4-column.html")

#vista de eventos
def eventos(request): 
    return render(request, "pagina/event-list.html")
