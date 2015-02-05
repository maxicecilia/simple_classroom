# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _


class StudentProfile(models.Model):
    user = models.OneToOneField(User)
    cx = models.CharField(max_length=8, null=False, blank=False)
    telephone = models.CharField(max_length=16, null=True, blank=True)

    def __unicode__(self):
        return u'{0}'.format(self.user.get_full_name())


class TeacherProfile(models.Model):
    user = models.OneToOneField(User)
    site = models.ForeignKey(Site)
    abstract = models.TextField(max_length=500, null=True, blank=True)


class Subject(models.Model):
    site = models.ForeignKey(Site)
    code = models.CharField(_(u'Código'), max_length=8, null=False, blank=False)
    name = models.CharField(_(u'Nombre'), max_length=30, null=False, blank=False)
    short_name = models.CharField(_(u'Nombre corto'), max_length=15, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Materia')
        verbose_name_plural = _(u'Materias')

    def __unicode__(self):
        return u'{}'.format(self.name)


class Dictation(models.Model):
    SEMESTER_CHOICES = (
        (1, _(u'Primero')),
        (2, _(u'Segundo')),
    )
    subject = models.ForeignKey(Subject)
    date_from = models.DateField(_('Desde'), null=True, blank=True)
    date_to = models.DateField(_('Hasta'), null=True, blank=True)
    semester = models.IntegerField(_('Semestre'), choices=SEMESTER_CHOICES, default=1, null=False, blank=False)
    year = models.IntegerField(_(u'Año'), null=False, blank=False)
    is_registration_open = models.BooleanField(_(u'Registración abierta'), default=True, null=False, blank=False)

    class Meta:
        verbose_name = _(u'Dictado')
        verbose_name_plural = _(u'Dictados')

    def __unicode__(self):
        return u'{0} {1}'.format(self.subject, self.year)


class Enrolled(models.Model):
    student_profile = models.ForeignKey(StudentProfile, null=False, blank=False)
    dictation = models.ForeignKey(Dictation, null=False, blank=False)
    date = models.DateField()
    previous_attempts = models.IntegerField(default=0)

    class Meta:
        verbose_name = _(u'Inscripto')
        verbose_name_plural = _(u'Inscriptos')

    def __unicode__(self):
        return u'{0}'.format(self.student_profile)


class Assignment(models.Model):
    ASSIGNMENT_TYPES = (
        (1, _(u'Final')),
        (2, _(u'Laboratorio')),
        (3, _(u'Parcial')),
        (4, _(u'Práctico')),
        (5, _(u'Quizz')),
    )
    dictation = models.ForeignKey(Dictation)
    title = models.CharField(_(u'Título'), max_length=255, blank=False, null=False)
    is_published = models.BooleanField(_(u'Publicado'), blank=False, null=False, default=False)
    publication_date = models.DateTimeField(_(u'Fecha de publicación'), blank=True, null=True)
    assignment_type = models.IntegerField(_('Tipo'), choices=ASSIGNMENT_TYPES, default=4, null=False, blank=False)

    class Meta:
        verbose_name = _(u'Asignación')
        verbose_name_plural = _(u'Asignaciones')

    def __unicode__(self):
        return u'{}'.format(self.title)


class Score(models.Model):
    assignment = models.ForeignKey(Assignment)
    enrolled = models.ForeignKey(Enrolled)
    date = models.DateTimeField(blank=False, null=False)
    value = models.IntegerField(blank=False, null=False)
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = _(u'Nota')
        verbose_name_plural = _(u'Notas')

    def __unicode__(self):
        return u'{0}-{1}-{2}'.format(self.enrolled.student_profile.user.get_full_name(), self.assignment, self.value)
