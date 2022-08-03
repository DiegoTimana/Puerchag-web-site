from django.contrib import admin
from .models import Acudiente, Asignatura, Cita, Curso, Estudiante, Evento, Nota, Profesor, Sugerencia, Usuario

# Register your models here. Esto sirve para ver las tablas en el administrador de django

admin.site.register(Usuario)
admin.site.register(Acudiente)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Asignatura)
admin.site.register(Estudiante)
admin.site.register(Nota)
admin.site.register(Cita)
admin.site.register(Sugerencia)
admin.site.register(Evento)


