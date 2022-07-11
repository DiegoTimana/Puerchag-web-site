# Generated by Django 3.1.3 on 2022-07-10 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignatura',
            name='id_curso',
        ),
        migrations.RemoveField(
            model_name='cita',
            name='id_acudiente',
        ),
        migrations.RemoveField(
            model_name='cita',
            name='id_profesor',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='id_profesor',
        ),
        migrations.DeleteModel(
            name='Escuela',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='id_acudiente',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='id_curso',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='id_profesor',
        ),
        migrations.RemoveField(
            model_name='nota',
            name='id_asignatura',
        ),
        migrations.RemoveField(
            model_name='nota',
            name='id_estudiante',
        ),
        migrations.RemoveField(
            model_name='sugerencia',
            name='id_acudiente',
        ),
        migrations.DeleteModel(
            name='Acudiente',
        ),
        migrations.DeleteModel(
            name='Asignatura',
        ),
        migrations.DeleteModel(
            name='Cita',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Evento',
        ),
        migrations.DeleteModel(
            name='Nota',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
        migrations.DeleteModel(
            name='Sugerencia',
        ),
    ]