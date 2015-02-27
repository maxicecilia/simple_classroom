# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from simple_classroom.apps.downloads import STORAGE
from simple_classroom.apps.core.models import DropboxStorageMixin
from simple_classroom.apps.classroom.models import Subject


class GroupCategory(models.Model):
    name = models.CharField(_(u'Nombre'), max_length=255, null=False, blank=False)
    order = models.IntegerField(_(u'Orden'))

    class Meta:
        verbose_name = _(u'Categoria')
        verbose_name_plural = _(u'Categorias')
        ordering = ['order', ]

    def __unicode__(self):
        return u'{}'.format(self.name)


class Book(models.Model, DropboxStorageMixin):
    author = models.CharField(_(u'Autor'), max_length=255, null=False, blank=False)
    category = models.ForeignKey(GroupCategory)
    edition = models.CharField(_(u'Edición'), max_length=255, null=False, blank=False)
    editorial = models.CharField(_(u'Editorial'), max_length=255, null=False, blank=False)
    cover_image = models.ImageField(_(u'Imagen'), upload_to='books', storage=STORAGE, null=True, blank=True)
    subject = models.ForeignKey(Subject)
    title = models.CharField(_(u'Titulo'), max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = _(u'Libro')
        verbose_name_plural = _(u'Libros')
        ordering = ['title', ]

    def __init__(self, *args, **kwargs):
        super(Book, self).__init__(*args, **kwargs)
        try:
            self.default_image = getattr(self, 'cover_image', None)
        except KeyError:
            pass

    def __unicode__(self):
        return u'{0}'.format(self.title)
