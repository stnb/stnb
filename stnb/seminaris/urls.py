# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import SeminariActualView, SeminariListView, SeminariDetailView, \
                   SeminariActualitzarView, \
                   TemaListView, TemaDetallView, DiaListView, DiaDetailView, \
                   XerradaLlistaView, XerradaDetallView, \
                   XerradaActualitzarView, XerradaFitxerActualitzarView

urlpatterns = patterns('',
    url(r'^actual/$', SeminariActualView.as_view(),
        name='seminari-actual'),
    url(r'^arxiu/$', SeminariListView.as_view(),
        name='seminari-llista'),

    url(r'^(?P<seminari_slug>[a-z0-9\-]+)/temes/$',
        TemaListView.as_view(), name='seminari-tema-llista'),
    url(r'^(?P<seminari_slug>[a-z0-9\-]+)/temes/(?P<tema_id>\d+)/$',
        TemaDetallView.as_view(), name='seminari-tema-detall'),
    url(r'^(?P<seminari_slug>[a-z0-9\-]+)/programa/$',
        DiaListView.as_view(), name='seminari-dia-llista'),
    url(r'^(?P<seminari_slug>[a-z0-9\-]+)/programa/(?P<dia_slug>[a-z0-9\-]+)/$',
        DiaDetailView.as_view(), name='seminari-dia-detall'),
#    url(r'(?P<seminari_slug>[a-z0-9\-]+)/xerrades/$',
#        XerradaLlistaView.as_view(), name='seminari-xerrada-llista'),
    url(r'^(?P<seminari_slug>[a-z0-9\-]+)/xerrades/(?P<xerrada_id>\d+)/$',
        XerradaDetallView.as_view(),
        name='seminari-xerrada-detall'),
    url(r'^(?P<seminari_slug>[a-z0-9\-]+)/xerrades/(?P<xerrada_id>\d+)/actualitzar/$',
        XerradaActualitzarView.as_view(), name='seminari-xerrada-actualitzar'),
    url(r'^(?P<seminari_slug>[a-z0-9\-]+)/xerrades/(?P<xerrada_id>\d+)/fixter-actualitzar/$',
        XerradaFitxerActualitzarView.as_view(),
        name='seminari-xerrada-fitxer-actualitzar'),
    
    url(r'^(?P<slug>[a-z0-9\-]+)/$',
        SeminariDetailView.as_view(),
        name='seminari-detall'),
    url(r'^(?P<slug>[a-z0-9\-]+)/actualitzar/$',
        SeminariActualitzarView.as_view(),
        name='seminari-actualitzar'),


)
