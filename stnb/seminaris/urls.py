# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

from .views import SeminariActualView, SeminariListView, SeminariDetailView, TemaListView, DiaListView, DiaDetailView, XerradaListView

urlpatterns = patterns('',
    url(r'actual/$', SeminariActualView.as_view(),
        name='seminari-actual'),
    url(r'arxiu/$', SeminariListView.as_view(),
        name='seminari-llista'),
    url(r'(?P<slug>[a-z0-9\-]+)/$', SeminariDetailView.as_view(),
        name='seminari-detall'),

    url(r'(?P<seminari_slug>[a-z0-9\-]+)/temes/',
        TemaListView.as_view(), name='seminari-tema-llista'),
    url(r'(?P<seminari_slug>[a-z0-9\-]+)/programa/',
        DiaListView.as_view(), name='seminari-dia-llista'),
    url(r'(?P<seminari_slug>[a-z0-9\-]+)/programa/(?P<dia_slug>[a-z0-9\-]+)/',
        DiaDetailView.as_view(), name='seminari-dia-detall'),
    
    url(r'(?P<seminari_slug>[a-z0-9\-]+)/xerrades/',
        XerradaListView.as_view(), name='seminari-xerrada-llista'),

)
