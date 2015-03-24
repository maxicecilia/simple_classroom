from __future__ import unicode_literals

import datetime

from django import template
from django.utils.html import avoid_wrapping
from django.utils.timezone import is_aware, utc
from django.utils.translation import ugettext, ungettext_lazy

register = template.Library()


@register.filter
def daysince(d, now=None):
    """
    Takes two datetime objects and returns the days between d and now
    as a nicely formatted string, e.g. "10 days".  If d occurs after now,
    then "0 days" is returned.
    Adapted from
    https://github.com/django/django/blob/master/django/utils/timesince.py
    """
    # Convert datetime.date to datetime.datetime for comparison.
    if not isinstance(d, datetime.datetime):
        d = datetime.datetime(d.year, d.month, d.day)
    if now and not isinstance(now, datetime.datetime):
        now = datetime.datetime(now.year, now.month, now.day)

    if not now:
        now = datetime.datetime.now(utc if is_aware(d) else None)

    delta = (now - d)
    # ignore microseconds
    since = delta.days * 24 * 60 * 60 + delta.seconds
    if since <= 0:
        # d is in the future compared to now, stop processing.
        return avoid_wrapping(ugettext('0 minutes'))
    days_count = since // (60 * 60 * 24)
    return avoid_wrapping(ungettext_lazy('%d day', '%d days') % days_count)
