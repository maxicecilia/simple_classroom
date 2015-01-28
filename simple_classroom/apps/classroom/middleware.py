from django.conf import settings
from django.contrib.sites.models import Site, RequestSite
from django.utils.functional import SimpleLazyObject


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

    def process_request(self, request):
        request.site = SimpleLazyObject(lambda: get_site(request))