# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Download, SiteDownload, CategoryDownload


class DownloadInlineAdmin(admin.TabularInline):
    model = Download


@admin.register(SiteDownload)
class SiteDownloadAdmin(admin.ModelAdmin):
    list_display = ('site', 'download_type', 'category', 'title')
    list_filter = ('site', 'download_type', )


@admin.register(CategoryDownload)
class CategoryDownloadAdmin(admin.ModelAdmin):
    pass
