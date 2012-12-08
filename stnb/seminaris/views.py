# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, RedirectView
from django.core.urlresolvers import reverse
from django.http import Http404

from .models import Seminari, Tema, Dia, Xerrada, ItemPrograma

class SeminariActualView(RedirectView):

    permanent = False
    queryset = True

    def get_redirect_url(self):
        try:
            seminari= Seminari.objects.filter(actiu=True)[0]
        except IndexError:
            raise Http404
        return reverse('seminari-detall', kwargs={ 'slug': seminari.slug })

class SeminariListView(ListView):
    model = Seminari
    context_object_name = 'seminaris'
    template_name = 'seminaris/seminari_llista.html'

    queryset = Seminari.objects.filter(actiu=True)

class SeminariDetailView(DetailView):
    model = Seminari
    context_object_name = 'seminari'
    template_name = 'seminaris/seminari_detall.html'

    queryset = Seminari.objects.filter(actiu=True)
    slug_field = 'slug'

class TemaListView(ListView):
    model = Tema
    context_object_name = 'tema'
    template_name = 'seminaris/tema_llista.html'

    # FIXME: Select only from *this* Seminari.
    queryset = Tema.objects.all()
    slug_field = 'slug'

class DiaListView(ListView):
    model = Dia
    context_obejct_name = 'dies'
    template_name = 'seminaris/dia_llista.html'

    # FIXME: Select only from *this* Seminari.
    queryset = Dia.objects.all()

class DiaDetailView(DetailView):
    model = Dia
    context_obejct_name = 'dia'
    template_name = 'seminaris/dia_detall.html'

    # FIXME: Select only from *this* Seminari.
    queryset = Dia.objects.all()

class XerradaListView(ListView):
    model = Xerrada
    context_object_name = 'xerrada'
    template_name = 'seminaris/xerrada_llista.html'

    # FIXME: Select only from *this* Seminari.
    queryset = Xerrada.objects.all()

