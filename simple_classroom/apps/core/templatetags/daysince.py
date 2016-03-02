from __future__ import unicode_literals

import datetime

from django import template
from django.utils.html import avoid_wrapping
from django.utils.timezone import is_aware, utc, localtime
from django.utils.translation import ugettext, ungettext_lazy

register = template.Library()


@register.filter
def daysince(d, now=None):
    """
    Takes two datetime objects and returns the days between d and now
    as a nicely formatted string, e.g. "10 days".  If d occurs after now,
    then "0 days" is returned.
    """
    #Check if now provided
    if not now:
        now = datetime.datetime.now(utc if is_aware(d) else None)

    #Apply local timezone to objects and then zero the time part to include
    #inconcluded days in the count
    now = localtime(now).replace(hour = 0, minute = 0, second = 0, microsecond = 0)
    d = localtime(d).replace(hour = 0, minute = 0, second = 0, microsecond = 0)

    #Check for negative delta
    if d > now:
        return avoid_wrapping(ugettext('0 days'))

    delta = now - d
    return avoid_wrapping(ungettext_lazy('%d day', '%d days') % delta.days)
