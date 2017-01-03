# -*- coding: utf-8 -*-
from django.forms import ModelForm
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

from contact_us.models import SimpleContact


class CaptchaContactForm(ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget())
    '''
    Cpatcha enabled default form model for collect contact data.
    '''
    class Meta:
        model = SimpleContact
        fields = ('from_name', 'from_email', 'from_phone', 'message')


class SimpleCaptchaContactForm(ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget(explicit=True))
    '''
    Cpatcha enabled simplified contact form, ignore phone input.
    '''
    class Meta:
        model = SimpleContact
        fields = ('from_name', 'from_email', 'message')