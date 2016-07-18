# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse

from .decorators import login_required
#from django.contrib.auth.decorators import login_required
from .views import RegistreView


urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login',
        { 'template_name': 'comptes/login.html', },
        name='comptes-login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'comptes/logged_out.html'}, name='comptes-logout'),
    url(r'^restablir-contrasenya/$', 'django.contrib.auth.views.password_reset',
        {'template_name': 'comptes/password_reset_form.html'},
        name='comptes-restablir-contrasenya'),
    url(r'^restablir-contrasenya/enviat/$', 'django.contrib.auth.views.password_reset_done',
        {'template_name': 'comptes/password_reset_done.html'},
        name='comptes-restablir-contrasenya-enviat'),

    url(r'^restablir-contrasenya/confirmar/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm',
        {'template_name': 'comptes/password_reset_confirm.html'},
        name='comptes-restablir-contrasenya-confirmar'),
    url(r'^restablir-contrasenya/fet/$', 'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'comptes/password_reset_complete.html'},
        name='comptes-restablir-contrasenya-fet'),

    url(r'registre/$', RegistreView.as_view(), name='comptes-registre'),
    url(r'registre/fet/$', TemplateView.as_view(template_name='comptes/registre_fet.html'),
        name='comptes-registre-fet'),
    
#    url(r'perfil/$', login_required(PerfilDetallView.as_view()),
#        name='comptes-perfil-detall'),
#    url(r'perfil/actualitzar/$', login_required(PerfilUpdateView.as_view()),
#        name='comptes-perfil-actualitzar'),
)
