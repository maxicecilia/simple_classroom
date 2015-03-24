# -*- coding: utf-8 -*-
import logging
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import urlresolvers
from django.db.models import Q
from django.http import Http404, HttpResponseServerError, HttpResponseBadRequest, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import View
from site_news.models import NewsItem
from simple_classroom.apps.classroom.models import (
    Dictation, Enrolled, StudentProfile, TeacherProfile, Assignment, Score)


class ClassroomView(View):

    def dispatch(self, *args, **kwargs):
        try:
            self.current_dictation = Dictation.objects.get_current_or_default(
                site=self.request.site, default_id=kwargs.get('dictation_id', None))
        except:
            self.current_dictation = None
        return super(ClassroomView, self).dispatch(*args, **kwargs)


class HomeView(ClassroomView):
    template_name = 'classroom/home.html'

    def get(self, request, *args, **kwargs):
        if not self.current_dictation:
            raise Http404
        news = NewsItem.objects_published.get_latest_by_site(site=request.site)
        return render_to_response(
            self.template_name,
            RequestContext(self.request, {
                'news': news,
                'now': datetime.datetime.now().date(),
                'current_dictation': self.current_dictation,
                'total_dictated_hours': self.current_dictation.get_total_dictated_hours(),
            })
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


class EnrollView(ClassroomView):
    def post(self, request, *args, **kwargs):
        self.student_id = kwargs.get('student_id')
        self.validate()  # run validations
        try:
            previous_attempts = Enrolled.objects.filter(
                student_profile__id=self.student_id,
                dictation__subject=self.current_dictation.subject,).count()
            enroll = Enrolled.objects.create(
                student_profile=StudentProfile.objects.get(pk=self.student_id),
                dictation=self.current_dictation,
                date=datetime.datetime.now(),
                previous_attempts=previous_attempts)

            return JsonResponse({'enroll_id': enroll.pk, 'status': 'success'})
        except Exception as e:
            logging.excetpion(e)
            return HttpResponseServerError(e.message)

    def validate(self, *args, **kwargs):
        if Enrolled.objects.filter(
                student_profile__id=self.student_id,
                dictation=self.current_dictation).count() > 0:
            raise HttpResponseBadRequest(u'El usuario ya fue registrado para este dictado.')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EnrollView, self).dispatch(*args, **kwargs)


class TeachersView(ClassroomView):
    template_name = 'classroom/teachers.html'

    def get(self, request, *args, **kwargs):
        teachers = TeacherProfile.objects.filter(dictation=self.current_dictation).order_by('order')
        return render_to_response(
            self.template_name,
            RequestContext(self.request, {
                'dictation': self.current_dictation,
                'teachers': teachers,
            })
        )


class UploadScoresView(ClassroomView):
    '''
    class Score(models.Model):
    assignment = models.ForeignKey(Assignment)
    enrolled = models.ForeignKey(Enrolled)
    date = models.DateTimeField(blank=False, null=False)
    value = models.IntegerField(blank=False, null=False)
    comment = models.CharField(max_length=255, blank=True, null=True)
    '''
    def post(self, request, *args, **kwargs):
        assignment_id = kwargs.get('assignment_id')
        uploaded_file = request.FILES['upfile']
        failed_uuid = ''
        uploaded_grades = 0

        assignment = Assignment.objects.get(pk=int(assignment_id))
        for grade in uploaded_file:
            uuid, score = grade.split(',')
            try:
                enrolled = Enrolled.objects.get(
                    student_profile__cx=uuid, dictation=assignment.dictation)
                Score.objects.create(
                    assignment=assignment,
                    enrolled=enrolled,
                    date=datetime.date.today(),
                    value=score,
                    comment='', )
                uploaded_grades += 1
            except Enrolled.DoesNotExist as e:
                failed_uuid += '{},'.format(uuid)
                logging.debug(e)
                logging.error('Couldnt find student {}'.format(uuid))

        messages.add_message(
            request, messages.SUCCESS,
            u'Se cargaron {} notas para la asignación {}.'.format(uploaded_grades, assignment.title))
        if failed_uuid != '':
            messages.add_message(
                request, messages.ERROR, u'Estudiantes no encontrados: {}'.format(failed_uuid))

        return HttpResponseRedirect(urlresolvers.reverse(
            'admin:classroom_assignment_change', args=(assignment_id,)))
