# -*- coding: utf-8 -*-
from django.urls import path, re_path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

from stnb.noticies.views import IniciView
from stnb.pagines.views import PaginaPlanaDetallView
from stnb.i18n.views import set_language

urlpatterns = [
    re_path(r'^setlang/', set_language, name='set-language'),
    re_path(r'^i18n/', include('django.conf.urls.i18n')),
    re_path(r'^tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
]

if settings.SERVE_MEDIA is True:
    urlpatterns += [
        re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]

urlpatterns += i18n_patterns(
    re_path(r'^(?P<slug>sobre-stnb)/$', PaginaPlanaDetallView.as_view(),
        name='pagina-plana'),

    re_path(r'^comptes/', include('stnb.comptes.urls')),
    re_path(r'^institucions/', include('stnb.institucions.urls')),
    re_path(r'^seminaris/', include('stnb.seminaris.urls')),
    re_path(r'^esdeveniments/', include('stnb.esdeveniments.urls')),
    re_path(r'^noticies/', include('stnb.noticies.urls')),
    re_path(r'^membres/', include('stnb.membres.urls')),
    re_path(r'^publicacions/', include('stnb.publicacions.urls')),
    re_path(r'^calendari/', include('stnb.calendari.urls')),
    re_path(r'^arxiu/', include('stnb.arxiu.urls')),
    re_path(r'^(?P<slug>temes-stnb-2015)/$', PaginaPlanaDetallView.as_view(),
        name='pagina-plana'),

    re_path(r'^$', IniciView.as_view(), name='inici'),
)
