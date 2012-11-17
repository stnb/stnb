# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.utils.encoding import smart_bytes

DJANGO_COMPONENT = os.environ.get('DJANGO_COMPONENT', 'site')
FILESYSTEM_ROOT = os.path.abspath(
                   os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
DIRNAME = FILESYSTEM_ROOT

ADMINS = (
    ('Hayden Stainsby', 'hds@caffeineconcepts.com'),
)
MANAGERS = ADMINS


TIME_ZONE = 'Europe/Madrid'
LANGUAGE_CODE = 'ca'
LANGUAGES = (
    ('ca', 'Català'),
    ('es', 'Castellano'),
    ('en', 'English'),
)

USE_I18N = True
USE_L10N = True
USE_TZ = True

SECRET_KEY = 'f%-(30mhl1qlj$$ah808vn(!fo68pfo6ykwxo)wjzg4rz^psi#'


SITE_ID = 1

MEDIA_ROOT = ''
MEDIA_URL = ''

STATIC_ROOT = ''
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'stnb.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'stnb.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'south',
    'hvad',
    'stnb.institucions',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

