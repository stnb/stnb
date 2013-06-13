# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _
from hvad.forms import TranslatableModelForm

from .models import Publicacio

class PublicacioNomFitxerForm(TranslatableModelForm):

    class Meta:
        model = Publicacio
        fields = ('nom', 'fitxer', 'isbn', 'data_publicacio')

