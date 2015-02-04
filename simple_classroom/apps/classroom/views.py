# -*- coding: utf-8 -*-
import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404, HttpResponseServerError
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import View
from site_news.models import NewsItem
from apps.classroom.models import Dictation, Enrolled, StudentProfile


class HomeView(View):
    template_name = 'classroom/home.html'

    def get(self, request, *args, **kwargs):
        news = NewsItem.objects_published.get_latest_by_site(site=request.site)
        return render_to_response(
            self.template_name,
            RequestContext(self.request, {'news': news, 'now': datetime.datetime.now().date()})
        )


class ProfileView(View):
    template_name = 'classroom/profile.html'

    def get(self, request, *args, **kwargs):
        available_dictations = None
        current_enrollments = None
        # TODO: Change this to have different views for each profile type. Don't use magic string you filthy muggle.
        try:
            profile = request.user.studentprofile
            profile_type = 'student'
        except:
            try:
                profile = request.user.teacherprofile
                profile_type = 'teacher'
            except:
                raise Http404("Profile not found")

        if profile_type == 'student':
            available_dictations = Dictation.objects.filter(~Q(enrolled__student_profile=profile.id), is_registration_open=True)
            current_enrollments = Enrolled.objects.filter(student_profile=profile.id)

        return render_to_response(
            self.template_name,
            RequestContext(self.request, {
                'profile': profile,
                'profile_type': profile_type,
                'available_dictations': available_dictations,
                'current_enrollments': current_enrollments
            })
        )

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileView, self).dispatch(*args, **kwargs)


class EnrollView(View):
    def post(self, request, *args, **kwargs):
        try:
            student_profile = StudentProfile.objects.get(pk=kwargs.get('student_id'))
            dictation = Dictation.objects.get(pk=kwargs.get('dictation_id'))
            previous_attempts = Enrolled.objects.filter(
                student_profile=student_profile,
                dictation__subject=dictation.subject,).count()
            enroll = Enrolled.objects.create(
                student_profile=student_profile,
                dictation=dictation,
                date=datetime.datetime.now(),
                previous_attempts=previous_attempts)

            return JsonResponse({'enroll_id': enroll.pk, 'status': 'success'})
        except Exception as e:
            import traceback; traceback.print_exc();  # TODO: Fix me.
            return HttpResponseServerError(e.message)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EnrollView, self).dispatch(*args, **kwargs)
