# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import BibliographyView

urlpatterns = patterns(
    '',
    url(r'^(?P<site>[A-Za-z]*)/bibliography/$', BibliographyView.as_view(), name="bibliography_main"),
)
