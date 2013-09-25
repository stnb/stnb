# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from emailusernames.forms import EmailUserCreationForm

class CrearUsuariForm(EmailUserCreationForm):
    nom = forms.CharField(label=_('first name'), max_length=50)
    cognoms = forms.CharField(label=_('surname'), max_length=100)

    class Meta:
        model = User
        fields = ('nom', 'cognoms', 'email', 'password1', 'password2',)
    

class PerfilUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)


