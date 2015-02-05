# -*- coding: utf-8 -*-
from simple_classroom.apps.core.middleware import get_site


def sitetree(request):
    if not request.site:
        request.site = get_site(request)
    try:
        menu_name = request.site.extendedsite.menu.alias
    except:
        menu_name = None  # TODO: do something
    return {'menu_name': menu_name}
