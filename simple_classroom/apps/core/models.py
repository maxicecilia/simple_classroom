# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.sites.models import Site
from sitetree.settings import MODEL_TREE


class ExtendedSite(models.Model):
    site = models.OneToOneField(Site)
    menu = models.ForeignKey(MODEL_TREE)

    def __unicode__(self):
        return u'Extended info for {0}'.format(self.site.name)


class DropboxStorageMixin(object):
    """Simple mixin to add a method to retrieve the public URL for a dropbox stored image."""

    def get_public_url(self, url):
        return url.replace('www.dropbox', 'dl.dropboxusercontent')

    def get_image_url(self):
        try:
            return self.get_public_url(self.default_image.url)
        except Exception:
            return ''
