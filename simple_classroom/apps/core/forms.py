from django import forms
from registration.forms import RegistrationForm


class StudentRegistrationForm(RegistrationForm):
    cx = forms.CharField()