# -*- coding: utf-8 -*-
from django.urls import re_path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from .views import RegistreView


urlpatterns = [
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='comptes/login.html'),
        name='comptes-login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(template_name='comptes/logged_out.html'),
        name='comptes-logout'),
    re_path(r'^restablir-contrasenya/$', auth_views.PasswordResetView.as_view(
        template_name='comptes/password_reset_form.html'),
        name='comptes-restablir-contrasenya'),
    re_path(r'^restablir-contrasenya/enviat/$', auth_views.PasswordResetDoneView.as_view(
        template_name='comptes/password_reset_done.html'),
        name='comptes-restablir-contrasenya-enviat'),

    re_path(r'^restablir-contrasenya/confirmar/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,40})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='comptes/password_reset_confirm.html'),
        name='password_reset_confirm'),
    re_path(r'^restablir-contrasenya/fet/$', auth_views.PasswordResetCompleteView.as_view(
        template_name='comptes/password_reset_complete.html'),
        name='comptes-restablir-contrasenya-fet'),

    re_path(r'registre/$', RegistreView.as_view(), name='comptes-registre'),
    re_path(r'registre/fet/$', TemplateView.as_view(template_name='comptes/registre_fet.html'),
        name='comptes-registre-fet'),
]
