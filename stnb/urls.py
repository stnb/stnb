# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings

from stnb.noticies.views import IniciView
from stnb.pagines.views import PaginaPlanaDetallView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stnb.views.home', name='home'),
    # url(r'^stnb/', include('stnb.foo.urls')),
    #url(r'^seminaris/', include('stnb.seminaris.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^setlang/', 'stnb.i18n.views.set_language', name='set-language'),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^tinymce/', include('tinymce.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.SERVE_MEDIA is True:
    urlpatterns += patterns('',
        (r'media/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': settings.MEDIA_ROOT }),
    )

urlpatterns += i18n_patterns('',
    #url(r'^$', TemplateView.as_view(template_name='base.html'), name='inici'),
    

    url(r'^(?P<slug>sobre-stnb)/$', PaginaPlanaDetallView.as_view(),
        name='pagina-plana'),

    url(r'^comptes/', include('stnb.comptes.urls')),
    url(r'^institucions/', include('stnb.institucions.urls')),
    url(r'^seminaris/', include('stnb.seminaris.urls')),
    url(r'^esdeveniments/', include('stnb.esdeveniments.urls')),
    url(r'^noticies/', include('stnb.noticies.urls')),
    url(r'^membres/', include('stnb.membres.urls')),
    url(r'^publicacions/', include('stnb.publicacions.urls')),
    url(r'^calendari/', include('stnb.calendari.urls')),
    url(r'^arxiu/', include('stnb.arxiu.urls')),
    url(r'^(?P<slug>temes-stnb-2015)/$', PaginaPlanaDetallView.as_view(),
        name='pagina-plana'),

    url(r'^$', IniciView.as_view(), name='inici'),
)

