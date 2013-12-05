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
                                                  'data-height': 170,}))

    class Meta:
        model = Xerrada
        fields = ('titol', 'abstracte', 'presentadors', 'altres_presentadors',
                  'presentacio', 'article',)

class XerradaFitxerForm(forms.ModelForm):
    
    class Meta:
        model = Xerrada
        fields = ('presentacio', 'article',)
