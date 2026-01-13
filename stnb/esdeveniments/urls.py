# -*- coding: utf-8 -*-
from django.urls import re_path

from .views import EsdevenimentDetailView, EsdevenimentFitxerActualitzarView

urlpatterns = [
    re_path(r'^(?P<slug>[a-z0-9\-]+)/fixter-actualitzar/$',
        EsdevenimentFitxerActualitzarView.as_view(),
        name='esdeveniment-fitxer-actualitzar'),
    re_path(r'^(?P<slug>[a-z0-9\-]+)/$',
        EsdevenimentDetailView.as_view(),
        name='esdeveniment-detall'),
]
