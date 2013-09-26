# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import NoticiesUltimesView

urlpatterns = patterns('',
    url(r'ultimes/$', NoticiesUltimesView.as_view(),
        name='noticies-ultimes'),
)
