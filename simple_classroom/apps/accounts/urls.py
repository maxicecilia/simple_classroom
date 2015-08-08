# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from registration.backends.simple.views import RegistrationView

from simple_classroom.apps.accounts.views import ProfileView, \
    StudentProfileView, TeacherProfileView
from simple_classroom.apps.classroom.forms import StudentRegistrationForm


urlpatterns = patterns(
    '',
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
    url(r'^student/profile/$', TeacherProfileView.as_view(), name='teacher-profile'),
    url(r'^teacher/profile/$', StudentProfileView.as_view(), name='student-profile'),
    url(
        r'^register/$',
        RegistrationView.as_view(form_class=StudentRegistrationForm),
        name='registration_register'),
    (r'', include('registration.backends.default.urls')),
)
