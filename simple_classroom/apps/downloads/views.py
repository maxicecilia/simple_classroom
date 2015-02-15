# -*- coding: utf-8 -*-
import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import View
from simple_classroom.apps.classroom.models import Dictation, Assignment
from simple_classroom.apps.downloads.models import Download


class DownloadsDictationView(View):
    template_name = 'downloads/per_dictation.html'

    def get(self, request, *args, **kwargs):
        dictation = Dictation.objects.get_current_or_default(
            site=request.site, default_id=kwargs.get('dictation_id', None))
        previous_dictations = Dictation.objects.filter(~Q(pk=dictation.pk)).order_by('-year')[:3]
        exercises = Assignment.objects.exercises().filter(dictation=dictation)
        midterms = Assignment.objects.published_midterms().filter(dictation__in=previous_dictations)
        return render_to_response(
            self.template_name,
            RequestContext(self.request, {
                'exercises': exercises,
                'dictation': dictation,
                'previous_dictations': previous_dictations,
                'midterms': midterms,
            })
        )

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DownloadsDictationView, self).dispatch(*args, **kwargs)
