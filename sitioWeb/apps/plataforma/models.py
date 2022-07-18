from django.db import models

# Create your models here.

class Escuela(models.Model):
    id_escuela = models.BigIntegerField (primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono_escuela = models.CharField(max_length=15)

class Profesor(models.Model):
    id_profesor = models.BigIntegerField (primary_key=True)
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    sexos = [
        ('F','Femenino'),
        ('M', 'Masculino')
    ]
    sexo_profesor = models.CharField(max_length=1, choices=sexos, default='F')
    email_profesor = models.EmailField()
    telefono_profesor = models.CharField(max_length=15)
    cargos = [('Profesor','Profesor'), ('Rector','Rector'), ('Administrador','Administrador')]
    cargo = models.CharField(max_length=20, choices=cargos, default='Profesor')
    estudios = [('Tecnico','Tecnico'),('Licenciatura','Licenciatura'),('Pregrado','Pregrado'),('Maestria','Maestria'),('Doctorado','Doctorado')]
    nivel_estudios = models.CharField(max_length=20, choices=estudios, default='Licenciatura')
    password = models.CharField(max_length=20)
    vigencia = models.BooleanField(default=True)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.id_profesor)

class Acudiente(models.Model):
    id_acudiente = models.BigIntegerField (primary_key=True)
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    vigencia = models.BooleanField(default=True)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.id_acudiente)


class Curso(models.Model):
    id_curso = models.BigIntegerField (primary_key=True)
    nombre = models.CharField(max_length=50)
    periodo_electivo = models.CharField(max_length=6)
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.id_curso)


class Asignatura(models.Model):
    id_asignatura = models.BigIntegerField (primary_key=True)
    nombre = models.CharField(max_length=50)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.id_asignatura)


class Estudiante(models.Model):
    id_estudiante = models.BigIntegerField (primary_key=True)
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    sexos = [
        ('F','Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    id_acudiente = models.ForeignKey(Acudiente, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.id_estudiante)


class Nota(models.Model):
    id_nota = models.BigIntegerField (primary_key=True)
    calificacion = models.DecimalField(max_digits=3, decimal_places=2)
    periodo = models.CharField(max_length=6)
    fecha = models.DateField()
    tipos = [('Parcial','Parcial'),('Quiz','Quiz'),('Tarea','Tarea'),('Trabajo','Trabajo')]
    tipo = models.CharField(max_length=20, choices=tipos, default='Tarea')
    comentario  = models.TextField()
    id_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.id_nota)

class Cita(models.Model):
    id_cita = models.BigIntegerField (primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    id_acudiente = models.ForeignKey(Acudiente, on_delete=models.CASCADE)
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.id_cita)


class Sugerencia(models.Model):
    id_sugerencia = models.BigIntegerField (primary_key=True)
    fecha_sugerencia = models.DateField()
    detalle_sugerencia = models.TextField()
    id_acudiente = models.ForeignKey(Acudiente, on_delete=models.CASCADE)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.id_sugerencia)


class Evento(models.Model):
    id_evento = models.BigIntegerField (primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    detalle = models.TextField()
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE) 

    def __str__(self):
        txt = "{0}"
        return txt.format(self.id_evento)