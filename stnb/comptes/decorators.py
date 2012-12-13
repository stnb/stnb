from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required as django_login_required

#from django.core import urlresolvers
#
#class lazy_string(object):
#    def __init__(self, function, *args, **kwargs):
#        self.function=function
#        self.args=args
#        self.kwargs=kwargs
#        
#    def __str__(self):
#        if not hasattr(self, 'str'):
#            self.str=self.function(*self.args, **self.kwargs)
#        return self.str
#
#def reverse(*args, **kwargs):
#    return lazy_string(urlresolvers.reverse, *args, **kwargs)
#
def login_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):

    if login_url is None:
        login_url = reverse_lazy('comptes-login')

    return django_login_required(function, redirect_field_name=redirect_field_name, login_url=login_url)
