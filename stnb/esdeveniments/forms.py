# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _

from .models import Esdeveniment

class EsdevenimentFitxerForm(forms.ModelForm):

    class Meta:
        model = Esdeveniment
        fields = ('presentacio', 'article',)

