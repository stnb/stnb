# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import ArxiuListView

urlpatterns = patterns('',
    url(r'^$', ArxiuListView.as_view(), name='arxiu'),
)
