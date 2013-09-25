# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _
from hvad.forms import TranslatableModelForm, \
                       TranslatableModelAllTranslationsForm
from tinymce.widgets import TinyMCE

from .models import Membre

#class MembreActualizarForm(TranslatableModelForm):
class MembreActualizarForm(TranslatableModelAllTranslationsForm):
    membre_des_de = forms.IntegerField(min_value=1900, max_value=2100,
            required=False,
            widget=forms.TextInput(attrs={'placeholder': _('Year'),
                                          'class': 'year-field'}))
    text = forms.CharField(label=_('Biography'), required=False,
                           widget=TinyMCE(attrs={'cols': 80, 'rows': 16}))

    class Meta:
        model = Membre
        fields = ('nom', 'cognoms', 'foto', 'afiliacio', 'membre_des_de',
                  'membre_actual', 'text', 'amagar_perfil', 'enllac',)
