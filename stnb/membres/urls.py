# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

from .views import MembreDetallView, MembreActualizarView

urlpatterns = patterns('',
    url(r'^(?P<slug>[a-z0-9\-]+)/$', MembreDetallView.as_view(),
        name='membre-detall'),
    url(r'^(?P<slug>[a-z0-9\-]+)/actualizar/$', MembreActualizarView.as_view(),
        name='membre-actualizar'),
)
