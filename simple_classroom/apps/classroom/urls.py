# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import EnrollView

urlpatterns = patterns(
    '',
    url(r'^enroll/(?P<dictation_id>\d*)/(?P<student_id>\d*)/$', EnrollView.as_view(), name="enroll_student"),
)
