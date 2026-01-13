# -*- coding: utf-8 -*-
from django.urls import re_path

from .views import CalendariListView

urlpatterns = [
    re_path(r'^$', CalendariListView.as_view(), name='calendari'),
]
