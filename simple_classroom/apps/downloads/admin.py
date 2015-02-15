# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Download


class DownloadInlineAdmin(admin.TabularInline):
    model = Download
