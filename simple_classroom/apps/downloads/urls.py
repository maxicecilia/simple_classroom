# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import DownloadsDictationView

urlpatterns = patterns(
    '',
    url(r'^(?P<site>[A-Za-z]*)/downloads/assignments/(?P<dictation_id>\d*)/$', DownloadsDictationView.as_view(), name="downloads_per_dictation"),
    url(r'^(?P<site>[A-Za-z]*)/downloads/assignments/$', DownloadsDictationView.as_view(), name="downloads_per_dictation_latest"),
)
