# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

from .views import InstitucioListView, InstitucioDetailView

urlpatterns = patterns('',
    url(r'^$', InstitucioListView.as_view(),
        name='institucio-llista'),
    url(r'^(?P<slug>[a-z0-9\-]+)/$', InstitucioDetailView.as_view(),
        name='institucio-detall'),
)
