# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, TemplateView, \
                                 RedirectView, UpdateView
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.http import Http404

from stnb.comptes.decorators import login_required
from .models import Seminari, Tema, Dia, Xerrada, ItemPrograma
from .forms import XerradaForm, XerradaFitxerForm

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

class TemaDetallView(TemplateView):
    template_name = 'seminaris/tema_detall.html'

    def get_context_data(self, **kwargs):
        context = super(TemaDetallView, self).get_context_data(**kwargs)
        
        seminari = get_object_or_404(Seminari, slug=kwargs['seminari_slug'])
        tema = get_object_or_404(Tema, pk=kwargs['tema_id'])
        if tema.seminari != seminari:
            raise Http404

        context.update({ 'seminari': seminari, 'tema': tema})

        return context

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

class XerradaLlistaView(TemplateView):
    template_name = 'seminaris/xerrada_llista.html'

    def get_context_data(self, **kwargs):
        context = super(XerradaLlistaView, self).get_context_data(**kwargs)

        seminari = get_object_or_404(Seminari, slug=kwargs['seminari_slug'])
        xerrades  = Xerrada.objects.filter(tema__seminari=seminari).distinct()

        context.update({ 'seminari': seminari, 'xerrades': xerrades })

        return context
   
class XerradaDetallView(TemplateView):
    template_name = 'seminaris/xerrada_detall.html'

    def get_context_data(self, **kwargs):
        context = super(XerradaDetallView, self).get_context_data(**kwargs)
        
        seminari = get_object_or_404(Seminari, slug=kwargs['seminari_slug'])
        xerrada = get_object_or_404(Xerrada, pk=kwargs['xerrada_id'])
        if xerrada.seminari() != seminari:
            raise Http404

        context.update({ 'seminari': seminari, 'xerrada': xerrada })

        return context

class XerradaActualitzarView(UpdateView):
    form_class = XerradaForm
    model = Xerrada
    template_name = 'seminaris/xerrada_actualitzar_form.html'

    queryset = Xerrada.objects.all()
    pk_url_kwarg = 'xerrada_id'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(XerradaActualitzarView, self).dispatch(*args, **kwargs)

    def get_object(self, *args, **kwargs):
        obj = super(XerradaActualitzarView, self).get_object(*args, **kwargs)
        if obj.is_owned_by(self.request.user) is False and self.request.user.is_staff is False:
            raise PermissionDenied
        return obj

#    def get(self, request, *args, **kwargs):
#        form_class = self.get_form_class()
#        form = self.get_form(form_class)
#        return self.render_to_response(self.get_context_data(form=form), **kwargs) 

    def get_context_data(self, **kwargs):
        context = super(XerradaActualitzarView, self).get_context_data(**kwargs)
        
        seminari = get_object_or_404(Seminari, slug=self.kwargs['seminari_slug'])
        xerrada = self.object
        if xerrada.seminari() != seminari:
            raise Http404

        context.update({ 'seminari': seminari, 'xerrada': xerrada })

        return context

class XerradaFitxerActualitzarView(UpdateView):
    form_class = XerradaFitxerForm
    model = Xerrada
    template_name = 'seminaris/xerrada_fitxer_actualitzar_form.html'

    queryset = Xerrada.objects.all()
    pk_url_kwarg = 'xerrada_id'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(XerradaFitxerActualitzarView, self).dispatch(*args, **kwargs)

    def get_object(self, *args, **kwargs):
        obj = super(XerradaFitxerActualitzarView, self).get_object(*args, **kwargs)
        if obj.is_owned_by(self.request.user) is False and self.request.user.is_staff is False:
            raise PermissionDenied
        return obj

#    def get(self, request, *args, **kwargs):
#        form_class = self.get_form_class()
#        form = self.get_form(form_class)
#        return self.render_to_response(self.get_context_data(form=form), **kwargs) 

    def get_context_data(self, **kwargs):
        context = super(XerradaFitxerActualitzarView, self).get_context_data(**kwargs)
        
        seminari = get_object_or_404(Seminari, slug=self.kwargs['seminari_slug'])
        xerrada = self.object
        if xerrada.seminari() != seminari:
            raise Http404

        context.update({ 'seminari': seminari, 'xerrada': xerrada })

        return context

