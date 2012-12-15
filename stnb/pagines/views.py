# -*- coding: utf-8 -*-
from django.views.generic import DetailView
from django.core.urlresolvers import reverse

from .models import PaginaPlana


class PaginaPlanaDetallView(DetailView):
    model = PaginaPlana
    context_object_name = 'pagina_plana'
    template_name = 'pagines/pagina_plana_detall.html'

    queryset = PaginaPlana.objects.all()
    slug_field = 'slug'
