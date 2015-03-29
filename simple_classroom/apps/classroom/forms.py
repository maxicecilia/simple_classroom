# -*- coding: utf-8 -*-
import logging
from django import forms
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from registration.forms import RegistrationFormUniqueEmail
from registration.signals import user_registered
from tinymce.widgets import TinyMCE
from simple_classroom.apps.classroom.models import StudentProfile, TeacherProfile


class StudentRegistrationForm(RegistrationFormUniqueEmail):
    first_name = forms.CharField(label=_(u'Nombre/s'))
    last_name = forms.CharField(label=_(u'Apellido'))
    cx = forms.CharField(label=_(u'CX'), help_text=_(u'Por favor, ingrese el CX sin guiones ni letras.'))
    telephone = forms.CharField(label=_(u'Teléfono'))


@receiver(user_registered)
def save_student_profile(sender, **kwargs):
    user = kwargs.get('user', None)
    request = kwargs.get('request')
    cx = request.POST.get('cx')
    if user:
        try:
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.save()
            StudentProfile.objects.create(
                user=user,
                telephone=request.POST.get('telephone'),
                cx=cx)
        except Exception as e:
            logging.error("An error ocurred while registering user {}, cx {}".format(user, cx))
            logging.exception(e)


class TeacherProfileForm(forms.ModelForm):
    abstract = forms.CharField(widget=TinyMCE(attrs={'cols': 100, 'rows': 20}))

    class Meta:
        model = TeacherProfile
        fields = ['user', 'dictation', 'abstract', 'avatar']
