# -*- coding: utf-8 -*-
from django import forms
from hvad.forms import TranslatableModelForm

from .models import Xerrada

class XerradaFitxerForm(forms.ModelForm):
    
    class Meta:
        model = Xerrada
        fields = ('presentacio', 'article',)

