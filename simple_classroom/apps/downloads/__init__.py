# -*- coding: utf-8 -*-
from django.conf import settings

DEFAULT_MEDIA_STORAGE = getattr(settings, 'DEFAULT_MEDIA_STORAGE', 'DROPBOX')
DEFAULT_MEDIA_STORAGE_LOCATION = getattr(settings, 'DEFAULT_MEDIA_STORAGE_LOCATION',
                                         '/simple_classroom')

if DEFAULT_MEDIA_STORAGE.upper() == 'DROPBOX':
    from django_dropbox.storage import DropboxStorage

    STORAGE = DropboxStorage(location=DEFAULT_MEDIA_STORAGE_LOCATION)
else:
    from django.core.files.storage import FileSystemStorage
    STORAGE = FileSystemStorage()
