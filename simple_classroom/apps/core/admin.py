# -*- coding: utf-8 -*-
from django.contrib import admin

from site_news.admin import NewsItemSimplifiedAdmin
from site_news.models import NewsItem
from simple_classroom.apps.core.models import ExtendedSite
from contact_us.admin import ContactUsAdmin
from contact_us.models import SimpleContact


admin.site.register(NewsItem, NewsItemSimplifiedAdmin)
admin.site.register(ExtendedSite)
admin.site.register(SimpleContact, ContactUsAdmin)
