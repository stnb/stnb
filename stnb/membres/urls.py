# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import MembreLlistaView, MembreDetallView, MembreActualitzarView

urlpatterns = patterns('',
    url(r'^$',
        MembreLlistaView.as_view(),
        name='membre-llista'),

    url(r'^(?P<slug>[a-z0-9\-]+)/$',
        MembreDetallView.as_view(),
        name='membre-detall'),

    url(r'^(?P<slug>[a-z0-9\-]+)/actualitzar/$',
        MembreActualitzarView.as_view(),
        name='membre-actualitzar'),
)
