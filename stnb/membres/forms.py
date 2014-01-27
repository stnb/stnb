# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _
from hvad.forms import TranslatableModelForm, \
                       TranslatableModelAllTranslationsForm
from tinymce.widgets import TinyMCE

from .models import Membre

class MembreBaseForm(forms.ModelForm):
    membre_des_de = forms.IntegerField(label=_('member since').capitalize(),
                                       required=False,
                                       min_value=1900, max_value=2100,
            widget=forms.TextInput(attrs={'placeholder': _('year'),
                                          'class': 'camp-any'}))

    class Meta:
        model = Membre
        fields = ('nom', 'cognoms', 'membre_des_de', 'afiliacio', 'enllac',
                   'amagar_perfil', 'membre_actual', 'foto',)

class MembreTranslationForm(forms.ModelForm):
    text = forms.CharField(required=False,
                           widget=TinyMCE(attrs={'cols': 70, 'rows': 12,}))
    language_code = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Membre._meta.translations_model

