# -*- coding: utf-8 -*-
from django.urls import re_path

from .views import InstitucioListView, InstitucioDetailView

urlpatterns = [
    re_path(r'^$', InstitucioListView.as_view(),
        name='institucio-llista'),
    re_path(r'^(?P<slug>[a-z0-9\-]+)/$', InstitucioDetailView.as_view(),
        name='institucio-detall'),
]
