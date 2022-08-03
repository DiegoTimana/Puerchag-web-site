from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
#el manager de los usuarios (para crear los super usuarios/usuarios basicos)
class UsuarioManager(BaseUserManager):
    def create_user(self,id,username,primer_apellido, segundo_apellido, email, telefono_profesor,
    es_profesor, es_acudiente, es_administrador, password):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        
        usuario = self.model(
            id = id,
            username = username,
            primer_apellido = primer_apellido,
            segundo_apellido = segundo_apellido,
            email = self.normalize_email(email),
            telefono_profesor = telefono_profesor,
            es_profesor = es_profesor,
            es_acudiente = es_acudiente,
            es_administrador = es_administrador
        )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, email, username, primer_apellido, id, password):
        usuario = self.create_user(
            email,
            username = username,
            primer_apellido = primer_apellido,
            id = id,
            password = password,   
     
        )
        usuario.es_administrador = True 
        usuario.save()
        return usuario

#usuario que va a servir para la autenticación
class Usuario(AbstractBaseUser):
    id = models.BigIntegerField(primary_key=True)#
    username = models.CharField(max_length=50)#
    primer_apellido = models.CharField(max_length=50)#
    segundo_apellido = models.CharField(max_length=50)#
    email = models.EmailField(unique=True, max_length=100)#
    telefono_profesor = models.CharField(max_length=15, blank=True, null=True)#
    # tipos_de_usuarios = [('Profesor','Profesor'), ('Rector','Rector'), ('Administrador','Administrador'),('Acudiente','Acudiente')]
    # tipo_de_usuario = models.CharField(max_length=20, choices=tipos_de_usuarios, default='Profesor')
    es_profesor = models.BooleanField(default=False)
    es_acudiente = models.BooleanField(default=False)
    es_administrador = models.BooleanField(default=False) #para ingresar al administrador de django
    vigencia = models.BooleanField(default=True)
    objects = UsuarioManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'primer_apellido', 'id']

    def __str__(self):
        return f'{self.id}'

    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.es_administrador


    def __str__(self):
        return f'{self.id}'


class Acudiente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)


class Profesor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)


# class Acudiente(models.Model):
#     id_acudiente = models.BigIntegerField(primary_key=True)
#     usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default='null')


class Curso(models.Model):
    id_curso = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    periodo_electivo = models.CharField(max_length=6)
    id_profesor = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id_curso}'


class Asignatura(models.Model):
    id_asignatura = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id_asignatura}'


class Estudiante(models.Model):
    id_estudiante = models.BigIntegerField(primary_key=True)
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
    id_acudiente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id_estudiante}'


class Nota(models.Model):
    id_nota = models.BigIntegerField(primary_key=True)
    calificacion = models.DecimalField(max_digits=3, decimal_places=2)
    periodo = models.CharField(max_length=6)
    fecha = models.DateField()
    titulo = models.CharField(max_length=40, null=True)
    comentario  = models.TextField(max_length=255, blank=True, null=True)
    id_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
       return f'{self.id_nota}'

class Cita(models.Model):
    id_cita = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    id_acudiente = models.ForeignKey(Acudiente, on_delete=models.CASCADE)
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id_cita}'


class Sugerencia(models.Model):
    id_sugerencia = models.BigIntegerField(primary_key=True)
    fecha_sugerencia = models.DateField()
    detalle_sugerencia = models.TextField(max_length=255)
    id_acudiente = models.ForeignKey(Acudiente, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id_sugerencia}'


class Evento(models.Model):
    id_evento = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    detalle = models.TextField(max_length=255)

    def __str__(self):
        return f'{self.id_evento}'