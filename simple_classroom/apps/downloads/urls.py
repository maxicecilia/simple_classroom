# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import DownloadsDictationView, SiteDownloadCategoryView, SiteDownloadView

urlpatterns = patterns(
    '',
    url(
        r'^(?P<site>[A-Za-z]*)/downloads/assignments/(?P<dictation_id>\d*)/$',
        DownloadsDictationView.as_view(),
        name="downloads_per_dictation"),
    url(
        r'^(?P<site>[A-Za-z]*)/downloads/assignments/$',
        DownloadsDictationView.as_view(), name="downloads_per_dictation_latest"),
    url(
        r'^(?P<site>[A-Za-z]*)/downloads/type/(?P<download_type>\d*)/$',
        SiteDownloadView.as_view(), name="downloads_per_site"),
    url(
        r'^(?P<site>[A-Za-z]*)/downloads/categories/$',
        SiteDownloadCategoryView.as_view(), name="downloads_per_category_all"),
    url(
        r'^(?P<site>[A-Za-z]*)/downloads/categories/type/(?P<download_type>\d*)/$',
        SiteDownloadCategoryView.as_view(), name="downloads_per_category"),
)
