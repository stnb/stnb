# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

from .views import NoticiesUltimesView

urlpatterns = patterns('',
    url(r'ultimes/$', NoticiesUltimesView.as_view(),
        name='seminari-llista'),
)
