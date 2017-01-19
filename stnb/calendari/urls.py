# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import CalendariListView

urlpatterns = patterns('',
    url(r'^$', CalendariListView.as_view(), name='calendari'),
)

