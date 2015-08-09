# -*- coding: utf-8 -*-
import logging
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import urlresolvers
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
    """
        Adds current dictation to the view instance.
    """
    def dispatch(self, *args, **kwargs):
        try:
            self.current_dictation = Dictation.objects.get_current_or_default(
                site=self.request.site, default_id=kwargs.get('dictation_id', None))
        except:
            self.current_dictation = None
        return super(ClassroomView, self).dispatch(*args, **kwargs)


class HomeView(ClassroomView):
    """ 127.0.0.1 """
    template_name = 'classroom/home.html'

    def get(self, request, *args, **kwargs):
        if not self.current_dictation:
            raise Http404
        news = NewsItem.objects_published.get_latest_by_site(site=request.site)
        return render_to_response(
            self.template_name,
            RequestContext(self.request, {
                'news': news,
                'now': datetime.datetime.now().date() - datetime.timedelta(days=2),
                'current_dictation': self.current_dictation,
                'total_dictated_hours': self.current_dictation.get_total_dictated_hours(),
            })
        )


class EnrollView(ClassroomView):
    """
        Allows to enroll a student into a dictation.
    """
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
    """
        Displays a list of teachers for the current dictation.
    """
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
    """
    Upload scores to given assignment.
    """
    def post(self, request, *args, **kwargs):
        assignment_id = kwargs.get('assignment_id')
        uploaded_file = request.FILES.get('upfile', False)
        failed_uuid = ''
        uploaded_grades = 0

        if assignment_id and uploaded_file:
            assignment = Assignment.objects.get(pk=int(assignment_id))
            for grade in uploaded_file:
                uuid, score = grade.split(',')
                try:
                    enrolled = Enrolled.objects.get(
                        student_profile__cx=uuid, dictation=assignment.dictation)
                    try:
                        score_obj = Score.objects.get(assignment=assignment, enrolled=enrolled)
                        score_obj.value = score
                        comment = u'Actualizada el día {}'.format(datetime.datetime.now())
                        score_obj.save()
                    except Score.DoesNotExist:
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

            # Add a negative score for all missing scores
            missing = Enrolled.objects.filter(
                dictation=assignment.dictation).exclude(
                student_profile__in=Score.objects.filter(assignment=assignment).values(
                    'enrolled__student_profile__pk'))
            for missing_enroll in missing:
                Score.objects.create(
                    assignment=assignment,
                    enrolled=missing_enroll,
                    date=datetime.date.today(),
                    value=-1,
                    comment=u'AUSENTE')

            messages.add_message(
                request, messages.SUCCESS,
                u'Se cargaron/actualizaron {} notas para la asignación {}.'.format(
                    uploaded_grades, assignment.title))
            messages.add_message(
                request, messages.WARNING,
                u'Se cargaron {} ausentes para la asignación {}.'.format(
                    missing.count(), assignment.title))
            if failed_uuid != '':
                messages.add_message(
                    request, messages.ERROR, u'Estudiantes no encontrados: {}'.format(
                        failed_uuid))
        else:
            messages.add_message(
                request, messages.ERROR,
                u'No se pudo procesar las notas. Por favor controle el archivo seleccionado e intente nuevamente')

        return HttpResponseRedirect(urlresolvers.reverse(
            'admin:classroom_assignment_change', args=(assignment_id,)))
