# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _
from hvad.forms import TranslatableModelAllTranslationsForm
from tinymce.widgets import TinyMCE

from .models import Xerrada

class XerradaForm(TranslatableModelAllTranslationsForm):
    titol = forms.CharField(label=_('title').capitalize() + ' (%(language)s)',
                            widget=forms.TextInput(attrs={'class':'titol'}))
    abstracte = forms.CharField(label=_('abstract').capitalize() + ' (%(language)s)',
                            required=False,
                            widget=TinyMCE(attrs={'cols': 80, 'rows': 16,
                                                  'data-width': 580,
                                                  'data-height': 170,
                                                  'style':'width:580px;height:170px;'},
                                           mce_attrs={'width': 580}))
    altres_presentadors = forms.CharField(widget=forms.TextInput(
                              attrs={'class':'altres-presentadors'}))

    class Meta:
        model = Xerrada
        fields = ('titol', 'abstracte', 'presentadors', 'altres_presentadors',
                  'presentacio', 'article',)

class XerradaBaseForm(forms.ModelForm):
    class Meta:
        model = Xerrada
        fields = ('presentadors', 'altres_presentadors',)

class XerradaTranslationForm(forms.ModelForm):
    titol = forms.CharField(label=_('title').capitalize(),
                            widget=forms.TextInput(attrs={'class':'titol'}))
    abstracte = forms.CharField(label=_('abstract').capitalize(),
                            required=False,
                            widget=TinyMCE(
                                           attrs={'cols': 80, 'rows': 20,
                                                  'data-width': 580,
                                                  'data-height': 170,},))
    language_code = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Xerrada._meta.translations_model

class XerradaFitxerForm(forms.ModelForm):
    
    class Meta:
        model = Xerrada
        fields = ('presentacio', 'article',)
