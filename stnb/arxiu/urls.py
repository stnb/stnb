# -*- coding: utf-8 -*-
from django.urls import re_path

from .views import ArxiuListView

urlpatterns = [
    re_path(r'^$', ArxiuListView.as_view(), name='arxiu'),
]
