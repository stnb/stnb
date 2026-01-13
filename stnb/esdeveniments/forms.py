# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import gettext as _

from .models import Esdeveniment

class EsdevenimentFitxerForm(forms.ModelForm):

    class Meta:
        model = Esdeveniment
        fields = ('presentacio', 'article',)

