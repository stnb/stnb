# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _
from hvad.forms import TranslatableModelForm
from tinymce.widgets import TinyMCE

from .models import Membre

class MembreActualizarForm(TranslatableModelForm):
    membre_des_de = forms.IntegerField(min_value=1900, max_value=2100,
            required=False,
            widget=forms.TextInput(attrs={'placeholder': _('Year'),
                                          'class': 'year-field'}))
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 12}))

    class Meta:
        model = Membre
        fields = ('nom', 'cognoms', 'foto', 'afiliacio',
                  'membre_des_de', 'membre_actual', 'text')
