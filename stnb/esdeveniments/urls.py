# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import EsdevenimentDetailView, EsdevenimentFitxerActualitzarView

urlpatterns = patterns('',
    url(r'^(?P<slug>[a-z0-9\-]+)/fixter-actualitzar/$',
        EsdevenimentFitxerActualitzarView.as_view(),
        name='esdeveniment-fitxer-actualitzar'),
    url(r'^(?P<slug>[a-z0-9\-]+)/$',
        EsdevenimentDetailView.as_view(),
        name='esdeveniment-detall'),
)
