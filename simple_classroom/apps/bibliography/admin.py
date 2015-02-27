# -*- coding: utf-8 -*-
from django.contrib import admin
from simple_classroom.apps.bibliography.models import Book, GroupCategory


@admin.register(GroupCategory)
class GroupCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
