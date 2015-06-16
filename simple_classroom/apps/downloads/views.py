# -*- coding: utf-8 -*-
import datetime
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import View
from simple_classroom.apps.classroom.models import Dictation, Assignment
from simple_classroom.apps.downloads.models import Download, SiteDownload, CategoryDownload


class DownloadsDictationView(View):
    ''' TODO: Move to classroom app'''
    template_name = 'downloads/per_dictation.html'

    def get(self, request, *args, **kwargs):
        dictation = Dictation.objects.get_current_or_default(
            site=request.site, default_id=kwargs.get('dictation_id', None))
        previous_dictations = Dictation.objects.filter(
            ~Q(pk=dictation.pk)).order_by('-year')[:2]
        exercises = Assignment.objects.exercises().filter(
            dictation=dictation).order_by('order')
        midterms = Assignment.objects.midterms().filter(
            dictation=dictation).order_by('-dictation__year')
        return render_to_response(
            self.template_name,
            RequestContext(self.request, {
                'exercises': exercises,
                'dictation': dictation,
                'previous_dictations': previous_dictations,
                'midterms': midterms,
            })
        )


class SiteDownloadCategoryView(View):
    template_name = 'downloads/per_category.html'

    def get(self, request, *args, **kwargs):
        result = list()
        download_type = None
        categories = CategoryDownload.objects.all()
        if 'download_type' in kwargs and kwargs['download_type'] != '':
            download_type = SiteDownload.DOWNLOAD_TYPES[int(kwargs.get('download_type'))][1]

        for category in categories:
            downloads = category.sitedownload_set.filter(site=request.site).order_by('title')
            if 'download_type' in kwargs and kwargs['download_type'] != '':
                downloads.filter(download_type=kwargs.get('download_type'))

            if downloads.count() > 0:
                result.append({
                    'category': category,
                    'downloads': downloads,
                })

        return render_to_response(
            self.template_name,
            RequestContext(self.request, {
                'site_downloads': result,
                'download_type': download_type
            })
        )


class SiteDownloadView(View):
    template_name = 'downloads/per_site.html'

    def get(self, request, *args, **kwargs):
        result = list()
        download_type = None
        if 'download_type' not in kwargs or kwargs['download_type'] == '':
            raise Http404

        download_type = SiteDownload.DOWNLOAD_TYPES[int(kwargs.get('download_type'))][1]
        downloads = SiteDownload.objects.filter(
            site=request.site,
            download_type=kwargs.get('download_type')).order_by('title')

        return render_to_response(
            self.template_name,
            RequestContext(self.request, {
                'site_downloads': downloads,
                'download_type': download_type
            })
        )
