# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, TemplateView, \
                                 RedirectView, UpdateView
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from hvad.utils import get_all_language_codes

from stnb.comptes.decorators import login_required
from .models import Seminari, Tema, Dia, Xerrada, ItemPrograma
from .forms import XerradaForm, XerradaFitxerForm, XerradaBaseForm, XerradaTranslationForm

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
   
class XerradaActualitzarView(TemplateView):
    template_name = 'seminaris/xerrada_actualitzar_form.html'

    def post(self, request, *args, **kwargs):
        seminari, xerrada = self.get_seminari_xerrada(**kwargs)

        form = self.get_shared_form(xerrada)
        trans_forms = self.get_translation_forms(xerrada)

        if form.is_valid():
            for tform in trans_forms:
                print 'tform:', tform.has_changed()
            return self.forms_valid(form, trans_forms)
        else:
            return self.forms_invalid(form, trans_forms)


    def get_context_data(self, **kwargs):
        context = super(XerradaActualitzarView, self).get_context_data(**kwargs)
        
        seminari, xerrada = self.get_seminari_xerrada(**kwargs)

        form = self.get_shared_form(xerrada)
        trans_forms = self.get_translation_forms(xerrada)

        context.update({ 'seminari': seminari, 'xerrada': xerrada,
                         'form': form, 'trans_forms': trans_forms })

        return context

    def forms_valid(self, form, trans_forms):
        obj = form.save()
        url = reverse('seminari-xerrada-actualitzar', kwargs={ 'seminari_slug': form.instance.seminari().slug, 'xerrada_id': form.instance.pk })
        return HttpResponseRedirect(url)

    def forms_invalid(self, form, trans_forms):
        return self.render_to_response(self.get_context_data(xerrada_id=form.instance.pk, seminari_slug=form.instance.seminari().slug))

    def get_seminari_xerrada(self, **kwargs):
        seminari = get_object_or_404(Seminari, slug=kwargs['seminari_slug'])
        xerrada = get_object_or_404(Xerrada, pk=kwargs['xerrada_id'])
        if xerrada.seminari() != seminari:
            raise Http404

        return seminari, xerrada

    def get_shared_form(self, shared_obj):
        form_args = { }
        if self.request.method in ('POST', 'PUT'):
            form_args.update({ 'data': self.request.POST,
                               'files': self.request.FILES })

        form = XerradaBaseForm(instance=shared_obj, **form_args)
        return form

    def get_translation_forms(self, shared_obj):
        trans_forms = [ ]

        form_args = { }
        if self.request.method in ('POST', 'PUT'):
            form_args.update({ 'data': self.request.POST,
                               'files': self.request.FILES })

        for lang in get_all_language_codes():
            trans = list(shared_obj.translations.filter(language_code=lang))
            if len(trans) == 0:
                print 'lang:', lang, 'trans:', None
                trans_form = XerradaTranslationForm(
                                 initial={'language_code':lang},
                                 prefix='trans_'+lang,
                                 **form_args)
            else:
                print 'lang:', lang, 'trans:', trans[0].titol
                trans_form = XerradaTranslationForm(
                                 instance=trans[0],
                                 prefix='trans_'+lang,
                                 **form_args)
            trans_forms.append(trans_form)

        return trans_forms

#    def validate_translation_forms(self, trans_forms):
#        for trans_form in trans_forms:
#            print "Language:", trans_forms.cleaned_data['language_code']




## class XerradaActualitzarView(UpdateView):
##     form_class = XerradaForm
##     model = Xerrada
##     template_name = 'seminaris/xerrada_actualitzar_form.html'
## 
##     queryset = Xerrada.objects.all()
##     pk_url_kwarg = 'xerrada_id'
##     
##     @method_decorator(login_required)
##     def dispatch(self, *args, **kwargs):
##         return super(XerradaActualitzarView, self).dispatch(*args, **kwargs)
## 
##     def get_object(self, *args, **kwargs):
##         obj = super(XerradaActualitzarView, self).get_object(*args, **kwargs)
##         if obj.is_owned_by(self.request.user) is False and self.request.user.is_staff is False:
##             raise PermissionDenied
##         return obj
## 
##     def get_context_data(self, **kwargs):
##         context = super(XerradaActualitzarView, self).get_context_data(**kwargs)
##         
##         seminari = get_object_or_404(Seminari, slug=self.kwargs['seminari_slug'])
##         xerrada = self.object
##         if xerrada.seminari() != seminari:
##             raise Http404
## 
##         context.update({ 'seminari': seminari, 'xerrada': xerrada })
## 
##         return context

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

