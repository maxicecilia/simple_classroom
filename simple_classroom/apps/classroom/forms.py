# -*- coding: utf-8 -*-
from django import forms
from registration.forms import RegistrationForm
from registration.signals import user_registered
from django.dispatch import receiver
from apps.classroom.models import StudentProfile


class StudentRegistrationForm(RegistrationForm):
    cx = forms.CharField(label=u'CX')
    telephone = forms.CharField(label=u'Teléfono')


@receiver(user_registered)
def save_student_profile(sender, **kwargs):
    user = kwargs.get('user', None)
    if user:
        try:
            StudentProfile.objects.create(
                user=user,
                telephone=kwargs.get('request').POST.get('telephone'),
                cx=kwargs.get('request').POST.get('cx'))
        except:
            pass  # TODO: log me!!
