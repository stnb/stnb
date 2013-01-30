# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, UpdateView, DetailView
from django.contrib.auth import authenticate, login

from emailusernames.forms import EmailUserCreationForm, EmailUserChangeForm
from emailusernames.utils import create_user

from stnb.membres.models import Membre
from .forms import CrearUsuariForm


class RegistreView(FormView):
    form_class = CrearUsuariForm
    template_name = 'comptes/registration_form.html'

    def form_valid(self, form):
        usuari = create_user(form.cleaned_data['email'],
                             form.cleaned_data['password1'])
        usuari.is_active = True
        usuari.save()

        membre = Membre(user=usuari,
                        nom=form.cleaned_data['nom'],
                        cognoms=form.cleaned_data['cognoms'])
        membre.save()

        # Asumim que el nou usuari és vàlid.
        nou_usuari = authenticate(email=form.cleaned_data['email'],
                                  password=form.cleaned_data['password1'])
        login(self.request, nou_usuari)

        return HttpResponseRedirect(reverse_lazy('membre-detall',
                                                 kwargs={'slug': membre.slug}))

#class PerfilDetallView(DetailView):
#    model = User
#    context_object_name = 'user'
#    template_name = 'comptes/perfil_detall.html'
#
#    def get_object(self, queryset=None):
#        if self.request.user.is_authenticated():
#            return self.request.user
#        else:
#            return HttpResponseRedirect(reverse_lazy('inici'))
#
#
#class PerfilUpdateView(UpdateView):
#    form_class = PerfilUpdateForm
#    model = User
#    template_name = 'comptes/perfil_actualitzar.html'
#    success_url = reverse_lazy('comptes-perfil-detall')
#
#    def get_object(self, queryset=None):
#        if self.request.user.is_authenticated():
#            return self.request.user
#        else:
#            return HttpResponseRedirect(reverse_lazy('inici'))
