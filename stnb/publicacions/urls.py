# -*- coding: utf-8 -*-
from django.urls import re_path

from .views import PublicacioLlistaView

urlpatterns = [
    re_path(r'^$', PublicacioLlistaView.as_view(),
        name='publicacio-llista'),
]
