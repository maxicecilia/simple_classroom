# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from simple_classroom.apps.classroom.models import Subject, Dictation, Enrolled, Assignment, Score
from simple_classroom.apps.downloads.admin import DownloadInlineAdmin


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


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'assignment_type', 'dictation', 'is_published', 'publication_date')
    list_filter = ('dictation', 'is_published', )
    inlines = [DownloadInlineAdmin, ]
    readonly_fields = ('publication_date', 'evaluation_date', 'score_date', )


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('student_full_name', 'assignment', 'value', 'comment', 'date')
    list_filter = ('assignment__dictation', 'assignment')

    def student_full_name(self, obj):
        return obj.enrolled.student_profile.user.get_full_name()
    student_full_name.short_description = _(u'Alumno')
