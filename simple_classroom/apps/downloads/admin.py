# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Download


class DownloadInlineAdmin(admin.TabularInline):
    model = Download
