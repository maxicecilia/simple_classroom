# -*- coding: utf-8 -*-
import logging
import datetime
import sys
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import urlresolvers
from django.db.models import Q
from django.http import Http404, HttpResponseServerError, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import View
from simple_classroom.apps.classroom.models import (
    Dictation, Enrolled, StudentProfile, TeacherProfile, Assignment, Score)

class ProfileView(View):
    template_name = 'classroom/profile.html'

    def get(self, request, *args, **kwargs):
        self.student_id = kwargs.get('student_id')

        available_dictations = None
        current_enrollments = None
        previous_enrollments = None
        # TODO: Change this to have different views for each profile type.
        # Don't use magic string you filthy muggle.
        try:
            profile = request.user.studentprofile
            profile_type = 'student'
            if self.student_id is not None:
                raise Http404("Operation not alowed")
        except:
            try:
                profile = request.user.teacherprofile
                profile_type = 'teacher'
                if self.student_id is not None:
                    profile = StudentProfile.objects.get(id=self.student_id)
                    profile_type = 'student'
            except:
                raise Http404("Profile not found")

        context = RequestContext(self.request, {
            'profile': profile,
            'profile_type': profile_type,
        })

        if profile_type == 'student':
            context.update(self._get_student_context(profile))
        if profile_type == 'teacher':
            context.update(self._get_teacher_context(profile))

        return render_to_response(
            self.template_name,
            context
        )

    def _get_student_context(self, profile):
        return {
            'available_dictations': Dictation.objects.filter(
                ~Q(enrolled__student_profile=profile.id), is_registration_open=True),
            'current_enrollments': Enrolled.objects.filter(
                student_profile=profile.id).filter(
                Q(dictation__date_to__gte=datetime.datetime.now) | Q(dictation__date_to=None)),
            'previous_enrollments': Enrolled.objects.filter(
                student_profile=profile.id, dictation__date_to__lt=datetime.datetime.now)
        }

    def _get_teacher_context(self, profile):
        return {
            'enrollments': Enrolled.objects.filter(dictation__teacherprofile=profile.id),
            'subject':''
        }

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileView, self).dispatch(*args, **kwargs)