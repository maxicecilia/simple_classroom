# -*- coding: utf-8 -*-
import datetime
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import View
from simple_classroom.apps.classroom.views import ClassroomView
from simple_classroom.apps.classroom.models import (
    Dictation, Enrolled, StudentProfile)


class AbstractProfileView(View):
    template_name = 'classroom/profile.html'
    profile_type = 'abstract'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AbstractProfileView, self).dispatch(*args, **kwargs)


class ProfileView(AbstractProfileView):
    """ Redirect to proper view. """
    def get(self, request, *args, **kwargs):
        pass
        try:
            request.user.teacherprofile
            return HttpResponseRedirect(reverse('teacher-profile'))
        except Exception as e:
            print e
            try:
                request.user.studentprofile
                return HttpResponseRedirect(reverse('student-profile'))
            except Exception as e:
                print e
                raise Http404("Profile not found")


class TeacherProfileView(AbstractProfileView):
    template_name = 'classroom/profile.html'

    def __init__(self, *args, **kwargs):
        super(TeacherProfileView, self).__init__(*args, **kwargs)
        self.profile_type = 'teacher'

    def get(self, request, *args, **kwargs):
        try:
            profile = request.user.teacherprofile
        except:
            raise Http404("Profile not found")

        context = RequestContext(self.request, {
            'profile': profile,
            'profile_type': self.profile_type,
            'dictations': Dictation.objects.get_open_dictations(),
        })

        return render_to_response(
            self.template_name,
            context
        )


class StudentProfileView(AbstractProfileView):

    def __init__(self, *args, **kwargs):
        super(StudentProfileView, self).__init__(*args, **kwargs)
        self.profile_type = 'student'

    def get(self, request, *args, **kwargs):
        available_dictations = None
        current_enrollments = None
        previous_enrollments = None
        try:
            profile = request.user.studentprofile
            profile_type = self.profile_type
        except:
            raise Http404("Profile not found")

        context = RequestContext(self.request, {
            'profile': profile,
            'profile_type': profile_type,
            'available_dictations': Dictation.objects.get_available_dictations(profile.id),
            'current_enrollments': Enrolled.objects.get_current_enrollments(profile.id),
            'previous_enrollments': Enrolled.objects.get_previous_enrollments(profile.id,)
        })

        return render_to_response(
            self.template_name,
            context
        )
