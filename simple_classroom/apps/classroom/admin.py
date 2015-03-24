# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from ordered_model.admin import OrderedModelAdmin
from simple_classroom.apps.classroom import models as class_models
from simple_classroom.apps.classroom.forms import TeacherProfileForm
from simple_classroom.apps.downloads.admin import DownloadInlineAdmin


def order_selected_objects(modeladmin, request, queryset):
    for index, obj in enumerate(queryset):
        obj.order = index + 1
        obj.save()
order_selected_objects.short_description = _('Ordenar objetos')


@admin.register(class_models.StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('student_last_name', 'student_first_name', 'cx', 'student_email', 'telephone', 'last_dictation')
    search_fields = ('student_profile__user__last_name', 'student_profile__cx', )

    def queryset(self, request):
        qs = super(StudentProfileAdmin, self).queryset(request)
        qs = qs.order_by('user__last_name', 'user__first_name')
        return qs

    def student_last_name(self, obj):
        return obj.user.last_name.title()
    student_last_name.short_description = _(u'Apellido')

    def student_first_name(self, obj):
        return obj.user.first_name.title()
    student_first_name.short_description = _(u'Nombre')

    def student_email(self, obj):
        return obj.user.email
    student_email.short_description = _(u'email')

    def last_dictation(self, obj):
        try:
            enroll = class_models.Enrolled.objects.filter(student_profile=obj).order_by('-dictation__year')[0]
            return enroll.dictation
        except IndexError:
            return '-'
    last_dictation.short_description = _(u'última inscripción')


@admin.register(class_models.TeacherProfile)
class TeacherProfileAdmin(OrderedModelAdmin):
    list_display = ('teacher_full_name', 'order', 'move_up_down_links', )
    form = TeacherProfileForm
    actions = [order_selected_objects]

    def teacher_full_name(self, obj):
        return obj.user.get_full_name()
    teacher_full_name.short_description = _(u'Profesor')


@admin.register(class_models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'site')


@admin.register(class_models.Dictation)
class DictationAdmin(admin.ModelAdmin):
    list_display = ('subject', 'year', 'semester', 'is_registration_open', 'enrolled_count', 'dictated_practice_hours', 'dictated_theory_hours', 'last_modification_date', 'date_from', 'date_to', )
    readonly_fields = ('last_modification_date', )
    list_filter = ('subject', )

    def enrolled_count(self, obj):
        return class_models.Enrolled.objects.filter(dictation=obj).count()
    enrolled_count.short_description = _(u'Inscriptos')


@admin.register(class_models.Enrolled)
class EnrolledAdmin(admin.ModelAdmin):
    list_display = (
        'student_last_name', 'student_first_name', 'student_cx',
        'student_email', 'previous_attempts', 'dictation')
    list_filter = ('dictation', )
    search_fields = ('student_profile__user__last_name', 'student_profile__cx', )

    def queryset(self, request):
        qs = super(EnrolledAdmin, self).queryset(request)
        qs = qs.order_by('student_profile__user__last_name', 'student_profile__user__first_name')
        return qs

    def student_last_name(self, obj):
        return obj.student_profile.user.last_name.title()
    student_last_name.short_description = _(u'Apellido')

    def student_first_name(self, obj):
        return obj.student_profile.user.first_name.title()
    student_first_name.short_description = _(u'Nombre')

    def student_cx(self, obj):
        return obj.student_profile.cx
    student_cx.short_description = _(u'cx')

    def student_email(self, obj):
        return obj.student_profile.user.email
    student_email.short_description = _(u'email')


@admin.register(class_models.Assignment)
class AssignmentAdmin(OrderedModelAdmin):
    list_display = (
        'title', 'assignment_type', 'dictation', 'is_published', 'publication_date', 'is_evaluated',
        'evaluation_date', 'is_scored', 'score_date', 'order', 'move_up_down_links', )
    list_filter = ('is_published', 'dictation', 'assignment_type', )
    inlines = [DownloadInlineAdmin, ]
    # readonly_fields = ('publication_date', 'evaluation_date', 'score_date', )
    actions = [order_selected_objects]


@admin.register(class_models.Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('student_full_name', 'assignment', 'value', 'comment', 'date')
    list_filter = ('assignment__dictation', 'assignment')

    def student_full_name(self, obj):
        return obj.enrolled.student_profile.user.get_full_name()
    student_full_name.short_description = _(u'Alumno')
