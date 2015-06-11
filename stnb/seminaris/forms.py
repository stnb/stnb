# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _
from tinymce.widgets import TinyMCE

from .models import Seminari, Xerrada

class SeminariBaseForm(forms.ModelForm):
    class Meta:
        model = Seminari
        fields = ('data_inici', 'data_finalizacio', 'actiu',
                  'organitzadors', 'altres_organitzadors', 'programa_pdf',)

class SeminariTranslationForm(forms.ModelForm):
    lloc = forms.CharField(#label=_('lloc').capitalize(),
                           required=False,
                           widget=TinyMCE(attrs={'cols': 80, 'rows': 20,}))
    language_code = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Seminari._meta.translations_model
        fields = '__all__'

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
        fields = '__all__'

class XerradaFitxerForm(forms.ModelForm):
    
    class Meta:
        model = Xerrada
        fields = ('presentacio', 'article',)
