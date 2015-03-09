# -*- coding: utf-8 -*-
import os
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext as _
from simple_classroom.apps.classroom.models import Assignment
from simple_classroom.apps.core.models import DropboxStorageMixin
from simple_classroom.apps.downloads import STORAGE


def get_upload_path(instance, filename):
    download_type = getattr(instance, 'download_type', 2)
    site = getattr(instance, 'site', None)
    return os.path.join(
        'files',
        site.subject.short_name if site else 'default',
        SiteDownload.FOLDERS[download_type],
        instance.data.name)


class Download(models.Model):
    ''' TODO: Change this name to a more specific one.'''
    assignment = models.ForeignKey(Assignment)
    title = models.CharField(_(u'Título'), max_length=255, blank=False, null=False)
    data = models.FileField(upload_to='files', storage=STORAGE, null=True, blank=True)
    upload_date = models.DateTimeField(_(u'Fecha de creación'), auto_now_add=True)

    class Meta:
        verbose_name = _(u'Descarga')
        verbose_name_plural = _(u'Descargas')

    def __unicode__(self):
        return u'{}'.format(self.title)


class CategoryDownload(models.Model):
    name = models.CharField(_(u'Nombre'), max_length=60, null=False, blank=False)
    order = models.IntegerField(_(u'Orden'), help_text=_(u'De menor a mayor, donde 0 es la primera posicion.'))

    class Meta:
        verbose_name = _(u'Categoría')
        verbose_name_plural = _(u'Categorías')
        ordering = ['-order', ]

    def __unicode__(self):
        return u'{}'.format(self.name)


class SiteDownload(models.Model, DropboxStorageMixin):
    ''' All downloads related to the site/subject'''
    SLIDE = _(u'Diapositivas')
    RESOURCE = _(u'Recursos para el alumno')
    OTHER = _(u'Otros')
    DOWNLOAD_TYPES = (
        (0, SLIDE),
        (1, RESOURCE),
        (2, OTHER),
    )
    FOLDERS = ('diapositivas/', 'resources/', 'others/')
    site = models.ForeignKey(Site)
    category = models.ForeignKey(CategoryDownload, verbose_name=_(u'Categoría'), null=True, blank=True)
    download_type = models.IntegerField(_(u'Tipo'), choices=DOWNLOAD_TYPES, default=4, null=False, blank=False)
    title = models.CharField(_(u'Título'), max_length=255, blank=False, null=False)
    data = models.FileField(upload_to=get_upload_path, storage=STORAGE, null=True, blank=True)
    upload_date = models.DateTimeField(_(u'Fecha de creación'), auto_now_add=True)

    def __init__(self, *args, **kwargs):
        super(SiteDownload, self).__init__(*args, **kwargs)
        try:
            self.default_image = getattr(self, 'data', None)
        except KeyError:
            pass

    class Meta:
        verbose_name = _(u'Descarga')
        verbose_name_plural = _(u'Descargas')

    def __unicode__(self):
        return u'{}'.format(self.title)
