# -*- coding: utf-8 -*-
import re
import os
import datetime

from django.db import models
from django.db.models import permalink
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from hvad.models import TranslatableModel, TranslatedFields

from stnb.seminaris.utils import persones_nom_cognoms, persones_html, \
                                 persones_text
from stnb.membres.models import Membre
from stnb.utils.text_processing import text_sense_accents

def nom_fitxer(ruta, nom):
    fitxer_nom = text_sense_accents(nom)
    return os.path.join(ruta, fitxer_nom)

def presentacio_nom_fitxer(esdeveniment, nom):
    ruta = 'esdeveniments/presentacions'
    fitxer_nom = nom_fitxer(ruta, nom)
    return fitxer_nom

def article_nom_fitxer(esdeveniment, nom):
    ruta = 'esdeveniments/articles'
    fitxer_nom = nom_fitxer(ruta, nom)
    return fitxer_nom

class Serie(TranslatableModel):
    slug = models.SlugField(_('slug'), max_length=50, blank=True)
    organitzadors = models.ManyToManyField(Membre, verbose_name=_('organisers'),
                                           related_name='series',
                                           blank=True)
    altres_organitzadors = models.CharField(_('other organisers'),
                                            max_length=250, blank=True,
                                            null=True)

    translations = TranslatedFields(
        nom = models.CharField(_('name'), max_length=50),
        descripcio = models.TextField(_('description'), blank=True, null=True),
    )

    class Meta:
        verbose_name = _('series')
        verbose_name_plural = _('series')

    def __unicode__(self):
        return self.nom

    def is_owned_by(self, user):
        owned_by = False
        membre = user.get_profile()
        if membre in self.organitzadors.all():
            owned_by = True
        return owned_by

    def nombre_de_esdeveniments(self):
        return self.esdeveniments.count()

    def organitzadors_html(self):
        return persones_html(
                list(self.organitzadors.all()) +
                     persones_nom_cognoms(self.altres_organitzadors))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super(Serie, self).save(*args, **kwargs)

class Esdeveniment(TranslatableModel):
    slug = models.SlugField(_('slug'), max_length=100, blank=True)
    serie = models.ForeignKey(Serie, verbose_name=_('serie'), blank=True,
                              null=True, related_name='esdeveniments')
    data = models.DateField(_('date'))
    hora_inici = models.TimeField(_('start time'), null=True, blank=True)
    hora_finalizacio = models.TimeField(_('end time'), null=True, blank=True)

    amfitrions = models.ManyToManyField(Membre, verbose_name=_('hosts'),
                                        related_name='esdeveniments_organizats',
                                        blank=True)
    altres_amfitrions = models.CharField(_('other hosts'), max_length=250,
                                         blank=True, null=True)
    presentadors = models.ManyToManyField(Membre, verbose_name=_('presenters'),
                                          related_name=
                                              'esdeveniments_presentats',
                                          blank=True)
    altres_presentadors = models.CharField(_('other presenters'),
                                           max_length=250, blank=True,
                                           null=True)

    presentacio = models.FileField(_('presentation'),
                                   upload_to=presentacio_nom_fitxer,
                                   blank=True, null=True)
    article = models.FileField(_('article'), upload_to=article_nom_fitxer,
                               blank=True, null=True)

    translations = TranslatedFields(
        titol = models.CharField(_('title'), max_length=255),
        abstracte = models.TextField(_('abstract'), blank=True, null=True),
        lloc = models.TextField(_('location'), blank=True, null=True),
    )

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')
        ordering = ['-data']

    def __unicode__(self):
        return self.titol

    @permalink
    def get_absolute_url(self):
        return ('esdeveniment-detall', (), {'slug': self.slug})

    def is_owned_by(self, user):
        owned_by = False
        membre = user.get_profile()
        if membre in self.amfitrions.all():
            owned_by = True
        elif membre in self.presentadors.all():
            owned_by = True
        elif self.serie is not None and self.serie.is_owned_by(user):
            owned_by = True
        return owned_by

    def amfitrions_html(self):
        return persones_html(
                list(self.amfitrions.all()) +
                     persones_nom_cognoms(self.altres_amfitrions))

    def presentadors_html(self):
        return persones_html(
                list(self.presentadors.all()) +
                     persones_nom_cognoms(self.altres_presentadors))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titol)
        super(Esdeveniment, self).save(*args, **kwargs)

