# -*- coding: utf-8 -*-
import datetime

from django.views.generic import DetailView, UpdateView
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator

from stnb.comptes.decorators import login_required
from .models import Esdeveniment
from .forms import EsdevenimentFitxerForm

class EsdevenimentDetailView(DetailView):
    model = Esdeveniment
    context_object_name = 'esdeveniment'
    template_name = 'esdeveniments/esdeveniment_detall.html'
    slug_field = 'slug'

class EsdevenimentFitxerActualitzarView(UpdateView):
    form_class = EsdevenimentFitxerForm
    model = Esdeveniment
    template_name = 'esdeveniments/esdeveniment_fitxer_actualitzar_form.html'

    queryset = Esdeveniment.objects.all()
    slug_field = 'slug'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EsdevenimentFitxerActualitzarView, self).dispatch(*args, **kwargs)

    def get_object(self, *args, **kwargs):
        obj = super(EsdevenimentFitxerActualitzarView, self).get_object(*args, **kwargs)
        if obj.is_owned_by(self.request.user) is False and self.request.user.is_staff is False:
            raise PermissionDenied
        return obj

#    def get_context_data(self, **kwargs):
#        context = super(EsdevenimentFitxerActualitzarView, self).get_context_data(**kwargs)
#
#        esdeveniment = self.object
#        context.update({ 'seminari': seminari, 'xerrada': xerrada })
#
#        return context
