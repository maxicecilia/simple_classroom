# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from simple_classroom.apps.classroom.models import Assignment
from simple_classroom.apps.downloads import STORAGE


class Download(models.Model):
    assignment = models.ForeignKey(Assignment)
    title = models.CharField(_(u'Título'), max_length=255, blank=False, null=False)
    data = models.FileField(upload_to='files', storage=STORAGE, null=True, blank=True)
    upload_date = models.DateTimeField(_(u'Fecha de creación'), auto_now_add=True)

    class Meta:
        verbose_name = _(u'Descarga')
        verbose_name_plural = _(u'Descargas')

    def __unicode__(self):
        return '{}'.format(self.title)
