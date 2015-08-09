# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from registration.backends.simple.views import RegistrationView

from simple_classroom.apps.accounts.views import ProfileView, \
    StudentProfileView, TeacherProfileView
from simple_classroom.apps.classroom.forms import StudentRegistrationForm


urlpatterns = patterns(
    '',
    url(r'^profile/(?:(?P<student_id>\d+)/)?$', ProfileView.as_view(), name='profile'),
    url(r'^teacher/profile/$', TeacherProfileView.as_view(), name='teacher-profile'),
    url(r'^student/profile/(?:(?P<student_id>\d+)/)?$', StudentProfileView.as_view(), name='student-profile'),
    url(
        r'^register/$',
        RegistrationView.as_view(form_class=StudentRegistrationForm),
        name='registration_register'),
    (r'', include('registration.backends.default.urls')),
)
