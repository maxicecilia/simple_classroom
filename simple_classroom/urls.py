# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from apps.classroom.views import HomeView, ProfileView
from apps.classroom.forms import StudentRegistrationForm
from registration.backends.simple.views import RegistrationView

urlpatterns = patterns(
    '',
    (r'', include('apps.classroom.urls')),
    # Accounts URLs
    url(r'^accounts/profile/$', ProfileView.as_view(), name='profile'),
    url(
        r'^accounts/register/$',
        RegistrationView.as_view(form_class=StudentRegistrationForm),
        name='registration_register'),
    (r'^accounts/', include('registration.backends.default.urls')),

    # Admin URLs
    url(r'^admin/', include(admin.site.urls)),

    # Site URLs
    url(r'^(?P<site>[A-Za-z]*)/$', HomeView.as_view(), name='home'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
