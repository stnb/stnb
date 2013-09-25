# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.db.models import permalink
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from hvad.models import TranslatableModel, TranslatedFields


class Noticia(TranslatableModel):
    data = models.DateTimeField(_('date'))

    creat = models.DateTimeField(_('created'), auto_now_add=True)
    actualizat = models.DateTimeField(_('updated'), auto_now=True)

    translations = TranslatedFields(
        titol = models.CharField(_('title'), max_length=255),
        descripcio = models.TextField(_('description')),
    )

    class Meta:
        verbose_name = _('news item')
        verbose_name_plural = _('news items')
        ordering = ['-data']

    def __unicode__(self):
        return self.titol

class MicroAlerta(TranslatableModel):
    data = models.DateTimeField(_('date'))

    creat = models.DateTimeField(_('created'), auto_now_add=True)
    actualizat = models.DateTimeField(_('updated'), auto_now=True)

    translations = TranslatedFields(
        alerta = models.TextField(_('alert')),
    )

    class Meta:
        verbose_name = _('microalert')
        verbose_name_plural = _('microalerts')
        ordering = ['-data']

    def __unicode__(self):
        return self.alerta


