from django.db import models
from django.contrib.sites.models import Site
from sitetree.settings import MODEL_TREE


class ExtendedSite(models.Model):
    site = models.OneToOneField(Site)
    menu = models.ForeignKey(MODEL_TREE)

    def __unicode__(self):
        return 'Extended {0}'.format(self.site.name)