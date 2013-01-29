# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _

from .models import Xerrada

class XerradaFitxerForm(forms.ModelForm):
    
    class Meta:
        model = Xerrada
        fields = ('presentacio', 'article',)
