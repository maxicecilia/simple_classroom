# -*- coding: utf-8 -*-
class DropboxStorageDeconstructible(object):
    def __init__(self, location=''):
        pass
"""
from django.conf import settings
from django.utils.deconstruct import deconstructible
from django_dropbox.storage import DropboxStorage


@deconstructible
class DropboxStorageDeconstructible(DropboxStorage):
    pass


DEFAULT_MEDIA_STORAGE = getattr(settings, 'DEFAULT_MEDIA_STORAGE', 'DROPBOX')
DEFAULT_MEDIA_STORAGE_LOCATION = getattr(settings, 'DEFAULT_MEDIA_STORAGE_LOCATION', '/simple_classroom')
if DEFAULT_MEDIA_STORAGE == 'DROPBOX':
    STORAGE = DropboxStorageDeconstructible(location=DEFAULT_MEDIA_STORAGE_LOCATION)
else:
    from django.core.files.storage import FileSystemStorage
    STORAGE = FileSystemStorage()
"""


def get_storage():
    from django.conf import settings
    from django.utils.deconstruct import deconstructible
    from django_dropbox.storage import DropboxStorage

    @deconstructible
    class DropboxStorageDeconstructible(DropboxStorage):
        pass

    DEFAULT_MEDIA_STORAGE = getattr(settings, 'DEFAULT_MEDIA_STORAGE', 'DROPBOX')
    DEFAULT_MEDIA_STORAGE_LOCATION = getattr(settings, 'DEFAULT_MEDIA_STORAGE_LOCATION', '/simple_classroom')
    if DEFAULT_MEDIA_STORAGE == 'DROPBOX':
        STORAGE = DropboxStorageDeconstructible(location=DEFAULT_MEDIA_STORAGE_LOCATION)
    else:
        from django.core.files.storage import FileSystemStorage
        STORAGE = FileSystemStorage()
    return STORAGE
