# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.db.models import permalink
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from hvad.models import TranslatableModel, TranslatedFields


class Noticia(TranslatableModel):
    data = models.DateTimeField()

    creat = models.DateTimeField(auto_now_add=True)
    actualizat = models.DateTimeField(auto_now=True)

    translations = TranslatedFields(
        titol = models.CharField(max_length=255),
        descripcio = models.TextField(),
    )

    class Meta:
        ordering = ['-data']
        verbose_name = 'notícia'
        verbose_name_plural = 'notícies'

    def __unicode__(self):
        return self.titol

class MicroAlerta(TranslatableModel):
    data = models.DateTimeField()

    creat = models.DateTimeField(auto_now_add=True)
    actualizat = models.DateTimeField(auto_now=True)

    translations = TranslatedFields(
        alerta = models.TextField(),
    )

    class Meta:
        ordering = ['-data']
        verbose_name = 'microalerta'
        verbose_name_plural = 'microalertes'

    def __unicdoe__(self):
        return self.alerta


