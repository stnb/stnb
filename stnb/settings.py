# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

FILESYSTEM_ROOT = os.path.dirname(__file__)
DIRNAME = FILESYSTEM_ROOT
## Import our defaults (globals)

from stnb.conf.settings.default import *  # NOQA

## Inherit from environment specifics
DJANGO_COMPONENT = os.environ.get('DJANGO_COMPONENT', 'site')
DJANGO_CONF = os.environ.get('DJANGO_CONF', 'default')
if DJANGO_CONF != 'default':
    module = __import__(DJANGO_CONF, globals(), locals(), ['*'])
    for k in dir(module):
        if not bytes(k).startswith('__'):
            globals()[k] = getattr(module, k)


## Import local settings

try:
    from .local_settings import *  # NOQA
except ImportError:
    import sys
    sys.stderr.write('No local_settings.py file found. You should COPY '
                     'local_settings.py.example to local_settings.py to '
                     'to get a development environment setup')

## Remove disabled apps

if 'DISABLED_APPS' in locals():
    INSTALLED_APPS = [k for k in INSTALLED_APPS if k not in DISABLED_APPS]

    MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
    try:
        DATABASE_ROUTERS = list(DATABASE_ROUTERS)
    except(NameError):
        DATABASE_ROUTERS = []

#    TEMPLATE_CONTEXT_PROCESSORS = list(TEMPLATE_CONTEXT_PROCESSORS)

    for a in DISABLED_APPS:
        for x, m in enumerate(MIDDLEWARE_CLASSES):
            if m.startswith(a):
                MIDDLEWARE_CLASSES.pop(x)

#        for x, m in enumerate(TEMPLATE_CONTEXT_PROCESSORS):
#            if m.startswith(a):
#                TEMPLATE_CONTEXT_PROCESSORS.pop(x)

        for x, m in enumerate(DATABASE_ROUTERS):
            if m.startswith(a):
                DATABASE_ROUTERS.pop(x)

#import djcelery
#djcelery.setup_loader()
