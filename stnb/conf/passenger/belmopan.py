import os, sys

ALLDIRS = ['/home/stnb/apps/env/stnb/lib/python2.7/site-packages']
INTERP = '/home/stnb/apps/env/stnb/bin/python'
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

import site

#sys.path = ALLDIRS

prev_sys_path = list(sys.path)

for directory in ALLDIRS:
    site.addsitedir(directory)

new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path
#print sys.path

os.environ['DJANGO_CONF'] = 'stnb.conf.settings.live'
os.environ['DJANGO_SETTINGS_MODULE'] = 'stnb.settings'

import django.core.handlers.wsgi
from paste.exceptions.errormiddleware import ErrorMiddleware

_application = django.core.handlers.wsgi.WSGIHandler()
application = ErrorMiddleware(_application, debug=True)

