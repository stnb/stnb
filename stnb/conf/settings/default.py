# -*- coding: utf-8 -*-
import os

from django.utils.translation import gettext_lazy as _

DJANGO_COMPONENT = os.environ.get('DJANGO_COMPONENT', 'site')
FILESYSTEM_ROOT = os.path.abspath(
                   os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
DIRNAME = FILESYSTEM_ROOT

ADMINS = [
    ('Hayden Stainsby', 'hds@caffeineconcepts.com'),
]
MANAGERS = ADMINS

TIME_ZONE = 'Europe/Madrid'
LANGUAGE_CODE = 'ca'
LANGUAGES = [
    ('ca', _('Catalan')),
    ('es', _('Spanish')),
    ('en', _('English')),
]

USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [
    os.path.join(DIRNAME, 'locale/'),
]

SECRET_KEY = 'f%-(30mhl1qlj$$ah808vn(!fo68pfo6ykwxo)wjzg4rz^psi#'

ALLOWED_HOSTS = ['stnb.cat', 'stnb.tk']

SITE_ID = 1
GA_TRACKER = 'UA-36931377-1'

SERVE_MEDIA = False
MEDIA_ROOT = ''
MEDIA_URL = '/media/'

STATIC_ROOT = ''
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(DIRNAME, 'static/'),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(DIRNAME, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'stnb.utils.context_processors.ganalytics_js',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

CACHALOT_ENABLED = True

AUTH_USER_MODEL = 'comptes.Usuari'

ROOT_URLCONF = 'stnb.urls'

WSGI_APPLICATION = 'stnb.wsgi.application'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'parler',
    'tinymce',
    'cachalot',
    'stnb.comptes',
    'stnb.institucions',
    'stnb.seminaris',
    'stnb.esdeveniments',
    'stnb.noticies',
    'stnb.membres',
    'stnb.publicacions',
    'stnb.pagines',
    'gunicorn',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Parler configuration (replacing hvad)
PARLER_LANGUAGES = {
    SITE_ID: (
        {'code': 'ca'},
        {'code': 'es'},
        {'code': 'en'},
    ),
    'default': {
        'fallbacks': ['ca'],
        'hide_untranslated': False,
    }
}

TINYMCE_DEFAULT_CONFIG = {
    'theme': 'silver',
    'relative_urls': False,
    'menubar': False,
    'toolbar': 'bold italic underline strikethrough | bullist numlist | link unlink | undo redo',
    'plugins': 'link lists',
    'content_css': STATIC_URL + '/css/stnb-editor.css',
    'body_id': 'editor-content',
}

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
