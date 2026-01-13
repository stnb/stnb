# -*- coding: utf-8 -*-
from django.urls import re_path

from .views import SeminariActualView, SeminariListView, SeminariDetailView, \
                   SeminariActualitzarView, \
                   TemaListView, TemaDetallView, DiaListView, DiaDetailView, \
                   XerradaLlistaView, XerradaDetallView, \
                   XerradaActualitzarView, XerradaFitxerActualitzarView

urlpatterns = [
    re_path(r'^actual/$', SeminariActualView.as_view(),
        name='seminari-actual'),
    re_path(r'^arxiu/$', SeminariListView.as_view(),
        name='seminari-llista'),

    re_path(r'^(?P<seminari_slug>[a-z0-9\-]+)/temes/$',
        TemaListView.as_view(), name='seminari-tema-llista'),
    re_path(r'^(?P<seminari_slug>[a-z0-9\-]+)/temes/(?P<tema_id>\d+)/$',
        TemaDetallView.as_view(), name='seminari-tema-detall'),
    re_path(r'^(?P<seminari_slug>[a-z0-9\-]+)/programa/$',
        DiaListView.as_view(), name='seminari-dia-llista'),
    re_path(r'^(?P<seminari_slug>[a-z0-9\-]+)/programa/(?P<dia_slug>[a-z0-9\-]+)/$',
        DiaDetailView.as_view(), name='seminari-dia-detall'),
    re_path(r'^(?P<seminari_slug>[a-z0-9\-]+)/xerrades/(?P<xerrada_id>\d+)/$',
        XerradaDetallView.as_view(),
        name='seminari-xerrada-detall'),
    re_path(r'^(?P<seminari_slug>[a-z0-9\-]+)/xerrades/(?P<xerrada_id>\d+)/actualitzar/$',
        XerradaActualitzarView.as_view(), name='seminari-xerrada-actualitzar'),
    re_path(r'^(?P<seminari_slug>[a-z0-9\-]+)/xerrades/(?P<xerrada_id>\d+)/fixter-actualitzar/$',
        XerradaFitxerActualitzarView.as_view(),
        name='seminari-xerrada-fitxer-actualitzar'),

    re_path(r'^(?P<slug>[a-z0-9\-]+)/$',
        SeminariDetailView.as_view(),
        name='seminari-detall'),
    re_path(r'^(?P<slug>[a-z0-9\-]+)/actualitzar/$',
        SeminariActualitzarView.as_view(),
        name='seminari-actualitzar'),
]
