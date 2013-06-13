# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, TemplateView, \
                                 RedirectView, UpdateView
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from .models import Publicacio

class PublicacioLlistaView(ListView):
    model = Publicacio
    context_object_name = 'publicacions'
    template_name = 'publicacions/publicacio_llista.html'

    queryset = Publicacio.objects.all()

