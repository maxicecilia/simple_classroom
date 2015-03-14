# -*- coding: utf-8 -*-
import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext as _
from ordered_model.models import OrderedModel
from tinymce.models import HTMLField
from simple_classroom.apps.core.models import DropboxStorageMixin
from simple_classroom.apps.downloads import STORAGE
from .managers import AssignmentManager, DictationManager


class StudentProfile(models.Model):
    user = models.OneToOneField(User)
    cx = models.CharField(max_length=8, null=False, blank=False)
    telephone = models.CharField(max_length=16, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Estudiante')
        verbose_name_plural = _(u'Estudiantes')

    def __unicode__(self):
        return u'{0}'.format(self.user.get_full_name())


class Subject(models.Model):
    site = models.OneToOneField(Site)
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
    dictated_practice_hours = models.PositiveIntegerField(_(u'Horas dictadas de práctica'), default=0, null=False, blank=False)
    dictated_theory_hours = models.PositiveIntegerField(_(u'Horas dictadas de teoría'), default=0, null=False, blank=False)
    last_modification_date = models.DateTimeField(_(u'Fecha de última modificación'), null=True, blank=True)

    objects = DictationManager()

    class Meta:
        verbose_name = _(u'Dictado')
        verbose_name_plural = _(u'Dictados')
        ordering = ['-year', 'subject']

    def __unicode__(self):
        return u'{0} {1}'.format(self.subject, self.year)

    def get_total_dictated_hours(self):
        return self.dictated_practice_hours + self.dictated_theory_hours

    def save(self, *args, **kwargs):
        if self.pk is not None:
            orig = Dictation.objects.get(pk=self.pk)
            if (orig.dictated_practice_hours != self.dictated_practice_hours
                    or orig.dictated_theory_hours != self.dictated_theory_hours):
                self.last_modification_date = datetime.datetime.now()
        super(Dictation, self).save(*args, **kwargs)


class TeacherProfile(models.Model, DropboxStorageMixin):
    abstract = HTMLField(null=True, blank=True)
    avatar = models.ImageField(_(u'Avatar'), upload_to='avatar', storage=STORAGE, null=True, blank=True)
    dictation = models.ManyToManyField(Dictation, verbose_name=_(u'Dictado'))
    user = models.OneToOneField(User, verbose_name=_(u'Usuario'))

    class Meta:
        verbose_name = _(u'Profesor')
        verbose_name_plural = _(u'Profesores')

    def __init__(self, *args, **kwargs):
        super(TeacherProfile, self).__init__(*args, **kwargs)
        try:
            self.default_image = getattr(self, 'avatar', None)
        except KeyError:
            pass

    def __unicode__(self):
        return u'{0}'.format(self.user.get_full_name())


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


class Assignment(OrderedModel):
    FINAL = _(u'Final')
    LABORATORY = _(u'Laboratorio')
    MIDTERM = _(u'Parcial')
    EXERCISE = _(u'Práctico')
    QUIZZ = _(u'Quizz')
    ASSIGNMENT_TYPES = (
        (1, FINAL),
        (2, LABORATORY),
        (3, MIDTERM),
        (4, EXERCISE),
        (5, QUIZZ),
    )
    dictation = models.ForeignKey(Dictation)
    title = models.CharField(_(u'Título'), max_length=255, blank=False, null=False)
    description = models.TextField(_(u'Descripción'), blank=True, null=True)
    is_published = models.BooleanField(
        _(u'Publicado'), blank=False, null=False, default=False,
        help_text=_(u'Tildar para mostrar la asignación a los inscriptos.'))
    publication_date = models.DateTimeField(_(u'Fecha de publicación'), blank=True, null=True)
    is_evaluated = models.BooleanField(
        _(u'Evaluado'), blank=False, null=False, default=False,
        help_text=_(u'Tildar para indicar que la evaluación ya fue tomada y está disponible.'))
    evaluation_date = models.DateTimeField(_(u'Fecha de evaluación'), blank=True, null=True)
    is_scored = models.BooleanField(
        _(u'Corregido'), blank=False, null=False, default=False,
        help_text=_(u'Tildar para indicar que la evaluación ya fue corregida y las notas están disponibles.'))
    score_date = models.DateTimeField(_(u'Fecha de Notas'), blank=True, null=True)
    assignment_type = models.IntegerField(_('Tipo'), choices=ASSIGNMENT_TYPES, default=4, null=False, blank=False)
    objects = AssignmentManager()

    class Meta(OrderedModel.Meta):
        verbose_name = _(u'Asignación')
        verbose_name_plural = _(u'Asignaciones')

    def __unicode__(self):
        return u'{}'.format(self.title)

    def save(self, *args, **kwargs):
        if self.pk is not None:
            orig = Assignment.objects.get(pk=self.pk)
            if orig.is_published != self.is_published and self.is_published is True:
                # TODO: trigger signal, create news
                self.publication_date = datetime.datetime.now()
            if orig.is_evaluated != self.is_evaluated and self.is_evaluated is True:
                # TODO: trigger signal, create news
                self.evaluation_date = datetime.datetime.now()
            if orig.is_scored != self.is_scored and self.is_scored is True:
                # TODO: trigger signal, create news
                self.score_date = datetime.datetime.now()

        super(Assignment, self).save(*args, **kwargs)

    def get_previous_assignments(self):
        ''' Returns the assignments for the last 2 previous dictations. '''
        return Assignment.objects.filter(
            is_published=True,
            assignment_type=self.assignment_type,
            title=self.title,
            dictation__in=Dictation.objects.filter(~Q(pk=self.dictation.pk)).order_by('-year')[:2],
        )

    def get_default_download(self):
        ''' Return the default download, you can set the title you want in the settings file. '''
        try:
            return self.download_set.get(title=getattr(settings, 'ASSIGNMENT_DEFAULT_DOWNLOAD', 'default'))
        except:
            return None


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
