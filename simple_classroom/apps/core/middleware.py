# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.sites.models import SiteManager, Site, RequestSite
from django.contrib.sites.shortcuts import get_current_site
from django.utils.functional import SimpleLazyObject
from . import get_current_request, set_thread_variable


def get_site(request):
    if not hasattr(request, '_cached_site'):
        domain = request.path.split('/')[1]
        try:
            site = Site.objects.get(domain=domain)
        except (Site.DoesNotExist, Site.MultipleObjectsReturned):
            try:
                site = Site.objects.get(pk=settings.SITE_ID)
            except Site.DoesNotExist:
                site = RequestSite(request)
        request._cached_site = site
    return request._cached_site


class RequestSiteMiddleware(object):

    def __init__(self):
        '''
            Override SiteManager.get_current to check for the request object first.
        '''
        def get_current_site(self, request=None):
            if (request and request.site):
                return request.site
            elif request:
                return SimpleLazyObject(lambda: get_site(request))

            request = get_current_request()
            return SimpleLazyObject(lambda: get_site(request))

        SiteManager.get_current = get_current_site

    def process_request(self, request):
        set_thread_variable('request', request)
        request.site = SimpleLazyObject(lambda: get_site(request))
