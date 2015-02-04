# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from apps.classroom.models import Subject, Dictation, Enrolled


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'site')


@admin.register(Dictation)
class DictationAdmin(admin.ModelAdmin):
    list_display = ('subject', 'year', 'semester', 'date_from', 'date_to')


@admin.register(Enrolled)
class EnrolledAdmin(admin.ModelAdmin):
    list_display = ('student_full_name', 'dictation', )
    list_filter = ('dictation', )

    def student_full_name(self, obj):
        return obj.student_profile.user.get_full_name()
    student_full_name.short_description = _(u'Alumno')
