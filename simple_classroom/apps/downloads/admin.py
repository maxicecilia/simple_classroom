# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Download, SiteDownload, CategoryDownload


class DownloadInlineAdmin(admin.TabularInline):
    model = Download


@admin.register(SiteDownload)
class SiteDownloadAdmin(admin.ModelAdmin):
    list_display = ('title', 'site', 'download_type', 'category', 'has_data', )
    list_filter = ('site', 'download_type', )

    def has_data(self, obj):
        return bool(obj.data)
    has_data.short_description = _(u'Archivo subido')
    has_data.boolean = True


@admin.register(CategoryDownload)
class CategoryDownloadAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
