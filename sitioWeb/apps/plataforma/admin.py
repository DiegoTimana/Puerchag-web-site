from django.contrib import admin
from .models import Escuela, Profesor, Acudiente, Curso, Asignatura, Estudiante, Nota, Cita, Sugerencia, Evento

# Register your models here.

admin.site.register(Escuela)
admin.site.register(Profesor)
admin.site.register(Acudiente)
admin.site.register(Curso)
admin.site.register(Asignatura)
admin.site.register(Estudiante)
admin.site.register(Nota)
admin.site.register(Cita)
admin.site.register(Sugerencia)
admin.site.register(Evento)

