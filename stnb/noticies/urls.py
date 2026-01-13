# -*- coding: utf-8 -*-
from django.urls import re_path

from .views import NoticiesUltimesView

urlpatterns = [
    re_path(r'ultimes/$', NoticiesUltimesView.as_view(),
        name='noticies-ultimes'),
]
