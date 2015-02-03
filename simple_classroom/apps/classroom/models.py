# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site


class StudentProfile(models.Model):
    user = models.OneToOneField(User)
    cx = models.CharField(max_length=8, null=False, blank=False)
    telephone = models.CharField(max_length=16, null=True, blank=True)


class Enrolled(models.Model):
    student_profile = models.ForeignKey(StudentProfile)
    site = models.ForeignKey(Site)
    date = models.DateField()
    previous_attempts = models.IntegerField(default=0)


class TeacherProfile(models.Model):
    user = models.OneToOneField(User)
    site = models.ForeignKey(Site)
    abstract = models.TextField(max_length=500, null=True, blank=True)
