# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, TemplateView
from django.core.urlresolvers import reverse
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from .models import Noticia, MicroAlerta
from stnb.pagines.models import PaginaPlana

class NoticiesUltimesView(ListView):
    model = Noticia
    context_object_name = 'noticies'
    template_name = 'noticies/noticies_ultimes_llista.html'

    queryset = Noticia.objects.all()[:10]

class IniciView(TemplateView):
    template_name = 'inici/inici.html'

    def get_context_data(self, **kwargs):
        context = super(IniciView, self).get_context_data(**kwargs)

        try:
            context['inici'] = PaginaPlana.objects.get(slug='inici')
        except ObjectDoesNotExist:
            pass
        context['noticies'] = Noticia.objects.all()[:10]
        context['microalertes'] = MicroAlerta.objects.all()[:1]

        return context


