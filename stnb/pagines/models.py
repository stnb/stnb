# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

class PaginaPlana(TranslatableModel):
    slug = models.SlugField(_('slug'), max_length=50)
    creat = models.DateTimeField(_('created'), auto_now_add=True)
    actualizat = models.DateTimeField(_('updated'), auto_now=True)

    translations = TranslatedFields(
        titol = models.CharField(_('title'), max_length=255),
        descripcio = models.TextField(_('description')),
    )

    class Meta:
        verbose_name = _('flat page')
        verbose_name_plural = _('flat pages')
        ordering = ['slug']

    def __str__(self):
        return self.titol
