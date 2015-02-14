# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import EnrollView, TeachersView

urlpatterns = patterns(
    '',
    url(r'^enroll/(?P<dictation_id>\d*)/(?P<student_id>\d*)/$', EnrollView.as_view(), name="enroll_student"),
    url(r'^(?P<site>[A-Za-z]*)/dictation/(?P<dictation_id>\d*)/teachers/$', TeachersView.as_view(), name="teacher_list_by_dictation"),
    url(r'^(?P<site>[A-Za-z]*)/teachers/$', TeachersView.as_view(), name="teacher_list"),
)
