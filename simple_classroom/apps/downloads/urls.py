# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page
from .views import DownloadsDictationView, SiteDownloadCategoryView, SiteDownloadView

urlpatterns = patterns(
    '',
    url(
        r'^(?P<site>[A-Za-z]*)/downloads/assignments/(?P<dictation_id>\d*)/$',
        cache_page(120 * 60)(DownloadsDictationView.as_view()),
        name="downloads_per_dictation"),
    url(
        r'^(?P<site>[A-Za-z]*)/downloads/assignments/$',
        cache_page(120 * 60)(DownloadsDictationView.as_view()), name="downloads_per_dictation_latest"),
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
