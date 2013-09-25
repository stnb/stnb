# -*- coding: utf-8 -*-
from django import forms
from hvad.forms import TranslatableModelForm

from .models import Publicacio

class PublicacioNomFitxerForm(TranslatableModelForm):

    class Meta:
        model = Publicacio
        fields = ('nom', 'fitxer', 'isbn', 'data_publicacio')

