# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


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

    def __str__(self):
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

    def __str__(self):
        return self.alerta
