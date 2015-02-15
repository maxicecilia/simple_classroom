# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.deconstruct import deconstructible
from django_dropbox.storage import DropboxStorage


@deconstructible
class DropboxStorageDeconstructible(DropboxStorage):
    pass


STORAGE = getattr(settings, 'DEFAULT_MEDIA_STORAGE', None)
if settings.DEBUG and not STORAGE:
    from django.core.files.storage import FileSystemStorage
    STORAGE = FileSystemStorage()
elif not STORAGE:
    STORAGE = DropboxStorageDeconstructible(location='/simple_classroom')
