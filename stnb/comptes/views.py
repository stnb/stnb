# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, UpdateView, DetailView

from emailusernames.forms import EmailUserCreationForm, EmailUserChangeForm
from emailusernames.utils import create_user

from .forms import PerfilUpdateForm


class RegistreView(FormView):
    form_class = EmailUserCreationForm
    template_name = 'comptes/registration_form.html'

    def form_valid(self, form):
        user = create_user(form.cleaned_data['email'],
                           form.cleaned_data['password1'])
        user.is_active = True
        user.save()

        return HttpResponseRedirect(reverse_lazy('comptes-registre-fet'))

class PerfilDetallView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'comptes/perfil_detall.html'

    def get_object(self, queryset=None):
        if self.request.user.is_authenticated():
            return self.request.user
        else:
            return HttpResponseRedirect(reverse_lazy('inici'))


class PerfilUpdateView(UpdateView):
    form_class = PerfilUpdateForm
    model = User
    template_name = 'comptes/perfil_actualizar.html'
    success_url = reverse_lazy('comptes-perfil-detall')

    def get_object(self, queryset=None):
        if self.request.user.is_authenticated():
            return self.request.user
        else:
            return HttpResponseRedirect(reverse_lazy('inici'))
