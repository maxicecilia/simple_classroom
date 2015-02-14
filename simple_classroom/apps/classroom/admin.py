# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from simple_classroom.apps.classroom import models as class_models
from simple_classroom.apps.classroom.forms import TeacherProfileForm
from simple_classroom.apps.downloads.admin import DownloadInlineAdmin


@admin.register(class_models.StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('student_full_name', 'cx', 'telephone')

    def student_full_name(self, obj):
        return obj.user.get_full_name()
    student_full_name.short_description = _(u'Alumno')


@admin.register(class_models.TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('teacher_full_name', )
    form = TeacherProfileForm

    def teacher_full_name(self, obj):
        return obj.user.get_full_name()
    teacher_full_name.short_description = _(u'Profesor')


@admin.register(class_models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'site')


@admin.register(class_models.Dictation)
class DictationAdmin(admin.ModelAdmin):
    list_display = ('subject', 'year', 'semester', 'date_from', 'date_to')


@admin.register(class_models.Enrolled)
class EnrolledAdmin(admin.ModelAdmin):
    list_display = ('student_full_name', 'dictation', )
    list_filter = ('dictation', )

    def student_full_name(self, obj):
        return obj.student_profile.user.get_full_name()
    student_full_name.short_description = _(u'Alumno')


@admin.register(class_models.Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'assignment_type', 'dictation', 'is_published', 'publication_date', 'is_evaluated', 'evaluation_date', 'is_scored', 'score_date')
    list_filter = ('dictation', 'is_published', )
    inlines = [DownloadInlineAdmin, ]
    readonly_fields = ('publication_date', 'evaluation_date', 'score_date', )


@admin.register(class_models.Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('student_full_name', 'assignment', 'value', 'comment', 'date')
    list_filter = ('assignment__dictation', 'assignment')

    def student_full_name(self, obj):
        return obj.enrolled.student_profile.user.get_full_name()
    student_full_name.short_description = _(u'Alumno')
