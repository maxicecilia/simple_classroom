# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from simple_classroom.apps.accounts.views import ProfileView
from simple_classroom.apps.classroom.forms import StudentRegistrationForm
from registration.backends.simple.views import RegistrationView

urlpatterns = patterns(
    '',
    url(r'^profile/(?:(?P<student_id>\d+)/)?$', ProfileView.as_view(), name='profile'),
    url(
        r'^register/$',
        RegistrationView.as_view(form_class=StudentRegistrationForm),
        name='registration_register'),
    (r'', include('registration.backends.default.urls')),
)
