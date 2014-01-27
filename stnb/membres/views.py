# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import UpdateView, DetailView, ListView
from django.http import Http404

from stnb.comptes.decorators import login_required
from stnb.utils.views import MultiTranslationFormView
from .forms import MembreBaseForm, MembreTranslationForm
from .models import Membre

class MembreLlistaView(ListView):
    model = Membre
    context_object_name = 'membres'
    template_name = 'membres/membre_llista.html'

    # Only current members who don't want their profile hidden are shown.
    queryset = Membre.objects.filter(amagar_perfil=False, membre_actual=True)

class MembreDetallView(DetailView):
    model = Membre
    context_object_name = 'membre'
    template_name = 'membres/membre_detall.html'

    # Past members can still have profiles, 
    queryset = Membre.objects.all() #filter(amagar_perfil=False)
    slug_field = 'slug'

    def get_object(self, *args, **kwargs):
        obj = super(MembreDetallView, self).get_object(*args, **kwargs)
        if obj.amagar_perfil is True and obj.user != self.request.user:
            raise Http404
        return obj

class MembreActualitzarView(MultiTranslationFormView):
    template_name = 'membres/membre_actualitzar_form.html'
    model = Membre
    shared_form_class = MembreBaseForm
    translation_form_class = MembreTranslationForm
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MembreActualitzarView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MembreActualitzarView, self).get_context_data(**kwargs)
        
        context.update({ 'membre': context['object'] })

        return context

    def get_object(self):
        membre = get_object_or_404(Membre, slug=self.kwargs['slug'])
        if membre.user != self.request.user:
            raise PermissionDenied
        return membre

