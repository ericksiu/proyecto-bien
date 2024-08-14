# Generated by Django 5.0.6 on 2024-06-28 05:30

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=12, verbose_name='Matricula')),
                ('nombre', models.TextField()),
                ('carrera', models.TextField()),
                ('turno', models.TextField(max_length=10)),
                ('edad', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografia')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Actualizado')),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ComentarioContacto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('usuario', models.TextField(verbose_name='Usuario')),
                ('mensaje', models.TextField(verbose_name='Comentario')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Registrado')),
            ],
            options={
                'verbose_name': 'Comentario Contacto',
                'verbose_name_plural': 'Comentarios Contactos',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Registrado')),
                ('coment', ckeditor.fields.RichTextField(verbose_name='Comentario')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.alumnos', verbose_name='Alumno')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
                'ordering': ['-created'],
            },
        ),
    ]
