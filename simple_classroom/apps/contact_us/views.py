# -*- coding: utf-8 -*-
from django.conf import settings
from contact_us.views import ContactUsFormView as ContactUsFormViewExt
from contact_us.forms import ContactForm, SimpleContactForm

from forms import CaptchaContactForm, SimpleCaptchaContactForm

class ContactUsFormView(ContactUsFormViewExt):

    def get_form_class(self):
        """
        Returns the form class to use in this view
        """
        if settings.CONTACT_US_FORM_STYLE == 'simple':
            self.form_class = SimpleContactForm
        if settings.CONTACT_US_FORM_STYLE == 'captcha':
            self.form_class = CaptchaContactForm
        if settings.CONTACT_US_FORM_STYLE == 'simplecaptcha':
            self.form_class = SimpleCaptchaContactForm
        return super(ContactUsFormView, self).get_form_class()