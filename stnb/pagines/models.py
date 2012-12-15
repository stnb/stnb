# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.db.models import permalink
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from hvad.models import TranslatableModel, TranslatedFields

class PaginaPlana(TranslatableModel):
    slug = models.SlugField(max_length=50)
    creat = models.DateTimeField(auto_now_add=True)
    actualizat = models.DateTimeField(auto_now=True)

    translations = TranslatedFields(
        titol = models.CharField(max_length=255),
        descripcio = models.TextField(),
    )

    class Meta:
        ordering = ['translations__titol']
        verbose_name = _('flat page') #'pàgina plana'
        verbose_name_plural = _('flat pages') #'pàgines planes'

    def __unicode__(self):
        return self.titol

