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

ugettext = lambda s: s

TIME_ZONE = 'Europe/Madrid'
LANGUAGE_CODE = 'ca'
LANGUAGES = (
    ('ca', ugettext('Catalan')),
    ('es', ugettext('Spanish')),
    ('en', ugettext('English')),
)

USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = (
    #PROJECT_DIR.child(locale)
    os.path.join(DIRNAME, 'locale/'),
)

SECRET_KEY = 'f%-(30mhl1qlj$$ah808vn(!fo68pfo6ykwxo)wjzg4rz^psi#'

ALLOWED_HOSTS = ['stnb.cat', 'stnb.tk']

SITE_ID = 1
GA_TRACKER = 'UA-36931377-1'

SERVE_MEDIA = False
MEDIA_ROOT = ''
MEDIA_URL = '/media/'

STATIC_ROOT = '' #os.path.join(DIRNAME, 'static/')
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(DIRNAME, 'static/'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'stnb.utils.context_processors.ganalytics_js',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


#CACHES = {
#    'default': {
#        'BACKEND': 'johnny.backends.memcached.MemcachedCache',
#        'LOCATION': ['127.0.0.1:11211'],
#        'JOHNNY_CACHE': True,
#    }
#}
#JOHNNY_MIDDLEWARE_KEY_PREFIX='jc_stnb'
CACHALOT_ENABLED = True


AUTH_USER_MODEL = 'comptes.Usuari'
#AUTHENTICATION_BACKENDS = (
#    'emailusernames.backends.EmailAuthBackend',
#)

AUTH_PROFILE_MODULE = 'membres.Membre'

ROOT_URLCONF = 'stnb.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'stnb.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(DIRNAME, 'templates/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'hvad',
    #'emailusernames',
    'tinymce',
    'cachalot',
    'raven.contrib.django',
    'stnb.comptes',
    'stnb.institucions',
    'stnb.seminaris',
    'stnb.esdeveniments',
    'stnb.noticies',
    'stnb.membres',
    'stnb.publicacions',
    'stnb.pagines',
    'gunicorn',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

#TINYMCE_JS_URL = MEDIA_URL + 'js/tiny_mce/tiny_mce.js'
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'relative_urls': False,
    'invalid_elements': 'span',
    'theme_advanced_toolbar_location': 'top',
    'theme_advanced_toolbar_align': 'center',
    'theme_advanced_buttons1': 'bold,italic,underline,strikethrough,separator,bullist,numlist,link,unlink,separator,undo,redo',
    'plugins': 'inlinepopups',
    'content_css': STATIC_URL + '/css/stnb-editor.css',
    'body_id': 'editor-content',
    
}
#}


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
            'handlers': [],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'
