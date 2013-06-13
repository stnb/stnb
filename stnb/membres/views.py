# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView, DetailView, ListView
from django.http import Http404

from stnb.comptes.decorators import login_required
from .forms import MembreActualizarForm
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
#    def get_object(self, queryset=None):
#        if self.request.user.is_authenticated():
#            return self.request.user
#        else:
#            return HttpResponseRedirect(reverse_lazy('inici'))


class MembreActualizarView(UpdateView):
    form_class = MembreActualizarForm
    model = Membre
    template_name = 'membres/membre_actualitzar_form.html'

    queryset = Membre.objects.all()
    slug_field = 'slug'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
#        if len(args) > 0:
#            request = args[0]
#        if kwargs['slug'] != request.user.get_profile().slug:
#            return HttpResponseForbidden()
        return super(MembreActualizarView, self).dispatch(*args, **kwargs)

    def get_object(self, *args, **kwargs):
        obj = super(MembreActualizarView, self).get_object(*args, **kwargs)
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj

