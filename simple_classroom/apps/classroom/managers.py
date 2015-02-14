# -*- coding: utf-8 -*-
from django.db import models


class AssignmentManager(models.Manager):
    def published_exercises(self):
        from .models import Assignment
        return super(AssignmentManager, self).get_queryset().filter(is_published=True, assignment_type=Assignment.ASSIGNMENT_TYPES[3][0])

    def published_midterms(self):
        from .models import Assignment
        return super(AssignmentManager, self).get_queryset().filter(is_published=True, assignment_type=Assignment.ASSIGNMENT_TYPES[2][0])
