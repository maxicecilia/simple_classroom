# -*- coding: utf-8 -*-
from django.contrib import admin

from site_news.admin import NewsItemSimplifiedAdmin
from site_news.models import NewsItem
from simple_classroom.apps.core.models import ExtendedSite


# Register your models here.
admin.site.register(NewsItem, NewsItemSimplifiedAdmin)
admin.site.register(ExtendedSite)
