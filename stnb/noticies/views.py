# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, TemplateView
from django.core.urlresolvers import reverse
from django.http import Http404

from .models import Noticia, MicroAlerta

class NoticiesUltimesView(ListView):
    model = Noticia
    context_object_name = 'noticies'
    template_name = 'noticies/noticies_ultimes_llista.html'

    queryset = Noticia.objects.all()[:10]

class IniciView(TemplateView):
    template_name = 'inici/inici.html'

    def get_context_data(self, **kwargs):
        context = super(IniciView, self).get_context_data(**kwargs)

        context['noticies'] = Noticia.objects.all()[:10]
        context['microalertes'] = MicroAlerta.objects.all()[:1]

        return context


