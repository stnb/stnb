# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, UpdateView, DetailView

from stnb.comptes.decorators import login_required
from .forms import MembreActualizarForm
from .models import Membre

class MembreDetallView(DetailView):
    model = Membre
    context_object_name = 'membre'
    template_name = 'membres/membre_detall.html'

    queryset = Membre.objects.all()
    slug_field = 'slug'

#    def get_object(self, queryset=None):
#        if self.request.user.is_authenticated():
#            return self.request.user
#        else:
#            return HttpResponseRedirect(reverse_lazy('inici'))


class MembreActualizarView(UpdateView):
    form_class = MembreActualizarForm
    model = Membre
    template_name = 'membres/membre_actualizar_form.html'

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

#    def post(self, request, *args, **kwargs):
#        form = self.form_class(request.POST, request.FILES)
#        if form.is_valid():
#            # file is saved
#            form.save()
#            print self.get_object()
#            return self.get_success_url()
#
#        return render(self.request, self.template_name,
#                self.context_data(**kwargs))
#
 
