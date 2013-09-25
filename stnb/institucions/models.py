# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from hvad.models import TranslatableModel, TranslatedFields

class Institucio(TranslatableModel):
    nom = models.CharField(_('name'), max_length=50)
    nom_curt = models.SlugField(_('short name'), max_length=10)
    url = models.CharField('URL', max_length=100)

    translations = TranslatedFields(
        descripcio = models.TextField(_('description')),
    )

    class Meta:
        verbose_name = _('institution')
        verbose_name_plural = _('institutions')

    def __unicode__(self):
        return self.nom_curt.upper()
