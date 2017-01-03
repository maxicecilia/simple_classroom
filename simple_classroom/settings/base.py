"""
Django settings for simple_classroom project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j$&8xx!udk6@yc$67^&s@1ie2mk2dfx+rnena=l^o=l)(ox367'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    'memcache_status',
    'bootstrap3',
    'django_dropbox',
    'registration',
    'site_news',
    'contact_us',
    'sitetree',
    'tinymce',
    'ordered_model',
    'snowpenguin.django.recaptcha2',
    'simple_classroom.apps.core',
    'simple_classroom.apps.classroom',
    'simple_classroom.apps.downloads',
    'simple_classroom.apps.bibliography',
    'simple_classroom.apps.accounts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'simple_classroom.apps.core.middleware.RequestSiteMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'simple_classroom.urls'

WSGI_APPLICATION = 'simple_classroom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-AR'

TIME_ZONE = 'America/Argentina/Tucuman'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',

    'sitesutils.context_processors.site',
    'simple_classroom.apps.core.context_processors.sitetree',
)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'simple_classroom/templates')]

SITE_ID = 1

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'simple_classroom/static'),
)

ACCOUNT_ACTIVATION_DAYS = 7  # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = False  # Automatically log the user in.
REGISTRATION_OPEN = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Dropbox config
DROPBOX_CONSUMER_KEY = ''
DROPBOX_CONSUMER_SECRET = ''

# Token for simple_classroom.
DROPBOX_ACCESS_TOKEN = ''
DROPBOX_ACCESS_TOKEN_SECRET = ''

# ReCaptcha Site and Secret keys.
RECAPTCHA_PRIVATE_KEY = ''
RECAPTCHA_PUBLIC_KEY = ''

# Title used to retrieve the default download file.
ASSIGNMENT_DEFAULT_DOWNLOAD = 'evaluativo'

# TinyMCE config
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,paste",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'fontsize_formats': "8pt 10pt 12pt 14pt 18pt 24pt 36pt",
    'theme_advanced_font_sizes': "10px,12px,13px,14px,16px,18px,20px",
    'font_size_style_values': "12px,13px,14px,16px,18px,20px",
}
TINYMCE_SPELLCHECKER = False
TINYMCE_COMPRESSOR = True

# Contact-us settings
CONTACT_US_RECIPIENTS_LIST = ['maxicecilia@gmail.com', ]
CONTACT_US_FORM_STYLE = 'simplecaptcha'

# Grappelli
GRAPPELLI_ADMIN_TITLE = u'Administracion'
GRAPPELLI_AUTOCOMPLETE_LIMIT = 10
GRAPPELLI_AUTOCOMPLETE_SEARCH_FIELDS = {
    "auth": {
        "user": ("username__icontains", "last_name__icontains", "first_name__icontains",)
    }
}

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
