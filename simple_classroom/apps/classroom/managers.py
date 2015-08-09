# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.db.models import Q


class AssignmentManager(models.Manager):
    def exercises(self):
        from .models import Assignment
        return super(AssignmentManager, self).get_queryset().filter(
            assignment_type=Assignment.ASSIGNMENT_TYPES[3][0])

    def midterms(self):
        from .models import Assignment
        return super(AssignmentManager, self).get_queryset().filter(
            assignment_type=Assignment.ASSIGNMENT_TYPES[2][0])

    def published_exercises(self):
        return self.exercises().filter(is_published=True)

    def published_midterms(self):
        return self.midterms().filter(is_published=True)


class DictationManager(models.Manager):
    def get_current_or_default(self, site, default_id=None):
        if default_id:
            return super(DictationManager, self).get_queryset().get(pk=default_id)
        else:
            return super(DictationManager, self).get_queryset().filter(
                subject__site=site).order_by('-year')[0]

    def get_available_dictations(self, student_profile_id):
        return super(DictationManager, self).get_queryset().filter(
            ~Q(enrolled__student_profile=student_profile_id),
            is_registration_open=True)

    def get_open_dictations(self):
        return super(DictationManager, self).get_queryset().filter(
            Q(date_to__gte=datetime.datetime.now) | Q(date_to=None))


class EnrolledManager(models.Manager):
    def get_current_enrollments(self, student_profile_id):
        return super(EnrolledManager, self).get_queryset().filter(
            student_profile=student_profile_id).filter(
            Q(dictation__date_to__gte=datetime.datetime.now) | Q(dictation__date_to=None))

    def get_previous_enrollments(self, student_profile_id):
        return super(EnrolledManager, self).get_queryset().filter(
            student_profile=student_profile_id,
            dictation__date_to__lt=datetime.datetime.now)
