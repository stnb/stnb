# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView

from .models import Seminari, Tema, Dia, Xerrada, ItemPrograma

class SeminariDetailView(DetailView):
    model = Institucio
    context_object_name = 'seminari'
    template_name = 'seminaris/seminari_detall.html'

    queryset = Seminari.objects.all()
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

