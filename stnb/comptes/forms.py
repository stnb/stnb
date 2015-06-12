# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _

class CrearUsuariForm(forms.ModelForm):
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = get_user_model()
        fields = ('nom', 'cognoms', 'email', 'password1', 'password2',)
    

class PerfilUpdateForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('nom', 'cognoms', 'email',)


