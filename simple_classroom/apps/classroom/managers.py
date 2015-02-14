# -*- coding: utf-8 -*-
from django.db import models


class AssignmentManager(models.Manager):
    def exercises(self):
        from .models import Assignment
        return super(AssignmentManager, self).get_queryset().filter(assignment_type=Assignment.ASSIGNMENT_TYPES[3][0])

    def midterms(self):
        from .models import Assignment
        return super(AssignmentManager, self).get_queryset().filter(assignment_type=Assignment.ASSIGNMENT_TYPES[2][0])

    def published_exercises(self):
        return self.exercises().filter(is_published=True)

    def published_midterms(self):
        return self.midterms().filter(is_published=True)
