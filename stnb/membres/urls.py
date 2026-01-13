# -*- coding: utf-8 -*-
from django.urls import re_path

from .views import MembreLlistaView, MembreDetallView, MembreActualitzarView

urlpatterns = [
    re_path(r'^$',
        MembreLlistaView.as_view(),
        name='membre-llista'),

    re_path(r'^(?P<slug>[a-z0-9\-]+)/$',
        MembreDetallView.as_view(),
        name='membre-detall'),

    re_path(r'^(?P<slug>[a-z0-9\-]+)/actualitzar/$',
        MembreActualitzarView.as_view(),
        name='membre-actualitzar'),
]
