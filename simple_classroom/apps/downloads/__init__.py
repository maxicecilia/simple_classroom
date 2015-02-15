# -*- coding: utf-8 -*-
from django.conf import settings

STORAGE = getattr(settings, 'DEFAULT_MEDIA_STORAGE', None)
if settings.DEBUG and not STORAGE:
    from django.core.files.storage import FileSystemStorage
    STORAGE = FileSystemStorage()
elif not STORAGE:
    STORAGE = DropboxStorageDeconstructible(location='/simple_classroom')
