# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='T\xedtulo')),
                ('is_published', models.BooleanField(default=False, verbose_name='Publicado')),
                ('publication_date', models.DateTimeField(null=True, verbose_name='Fecha de publicaci\xf3n', blank=True)),
                ('assignment_type', models.IntegerField(default=4, verbose_name='Tipo', choices=[(1, 'Final'), (2, 'Laboratorio'), (3, 'Parcial'), (4, 'Pr\xe1ctico'), (5, 'Quizz')])),
            ],
            options={
                'verbose_name': 'Asignaci\xf3n',
                'verbose_name_plural': 'Asignaciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dictation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_from', models.DateField(null=True, verbose_name='Desde', blank=True)),
                ('date_to', models.DateField(null=True, verbose_name='Hasta', blank=True)),
                ('semester', models.IntegerField(default=1, verbose_name='Semestre', choices=[(1, 'Primero'), (2, 'Segundo')])),
                ('year', models.IntegerField(verbose_name='A\xf1o')),
                ('is_registration_open', models.BooleanField(default=True, verbose_name='Registraci\xf3n abierta')),
            ],
            options={
                'verbose_name': 'Dictado',
                'verbose_name_plural': 'Dictados',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Enrolled',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('previous_attempts', models.IntegerField(default=0)),
                ('dictation', models.ForeignKey(to='classroom.Dictation')),
            ],
            options={
                'verbose_name': 'Inscripto',
                'verbose_name_plural': 'Inscriptos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('value', models.IntegerField()),
                ('comment', models.CharField(max_length=255, null=True, blank=True)),
                ('assignment', models.ForeignKey(to='classroom.Assignment')),
                ('enrolled', models.ForeignKey(to='classroom.Enrolled')),
            ],
            options={
                'verbose_name': 'Nota',
                'verbose_name_plural': 'Notas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cx', models.CharField(max_length=8)),
                ('telephone', models.CharField(max_length=16, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=8, verbose_name='C\xf3digo')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('short_name', models.CharField(max_length=15, null=True, verbose_name='Nombre corto', blank=True)),
                ('site', models.ForeignKey(to='sites.Site')),
            ],
            options={
                'verbose_name': 'Materia',
                'verbose_name_plural': 'Materias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('abstract', models.TextField(max_length=500, null=True, blank=True)),
                ('site', models.ForeignKey(to='sites.Site')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='enrolled',
            name='student_profile',
            field=models.ForeignKey(to='classroom.StudentProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dictation',
            name='subject',
            field=models.ForeignKey(to='classroom.Subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='dictation',
            field=models.ForeignKey(to='classroom.Dictation'),
            preserve_default=True,
        ),
    ]
