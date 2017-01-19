# -*- coding: utf-8 -*-
import re
import os
import datetime

from django.db import models
from django.db.models import permalink
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from hvad.models import TranslatableModel, TranslatedFields

from .utils import persones_nom_cognoms, persones_html, persones_text
from stnb.membres.models import Membre
from stnb.publicacions.models import Publicacio
from stnb.membres.utils import cognoms_lexic
from stnb.utils.text_processing import text_sense_accents

class Seminari(TranslatableModel):
    slug = models.SlugField(_('slug'), max_length=50)
    data_inici = models.DateField(_('start date'))
    data_finalizacio = models.DateField(_('end date'))
    organitzadors = models.ManyToManyField(Membre, verbose_name=_('organisers'),
                                           related_name='seminaris',
                                           blank=True)
    altres_organitzadors = models.CharField(_('other organisers'),
                                            max_length=250, blank=True,
                                            null=True)
    enllac_inscripcio = models.CharField(_('registration form'),
                                         max_length=250, blank=True, null=True)
    programa_pdf = models.FileField(_('programme PDF'),
                                    upload_to='seminaris/programes',
                                    blank=True, null=True)
    publicacio = models.ForeignKey(Publicacio, verbose_name=_('publication'),
                                   related_name='seminaris',
                                   blank=True, null=True)
    actiu = models.BooleanField(_('active'), default=False)
    
    translations = TranslatedFields(
        nom = models.CharField(_('name'), max_length=50),
        lloc = models.TextField(_('location')),
    )

    class Meta:
        verbose_name = _('seminar')
        verbose_name_plural = _('seminars')
        ordering = ['-data_inici']

    def __unicode__(self):
        return self.nom

    @permalink
    def get_absolute_url(self):
        return ('seminari-detall', (), {'slug': self.slug})

    def duracio(self):
        dstr = ''
        if self.data_inici.year == self.data_finalizacio.year:
            if self.data_inici.month == self.data_finalizacio.month:
                dstr= _('%(idia)s %(idata)d to %(fdia)s %(fdata)d %(imes)s, %(iany)d')
            else:
                dstr= _('%(idia)s %(idata)d %(imes)s to %(fdia)s %(fdata)d %(fmes)s, %(iany)d')
        else:
            dstr= _('%(idia)s %(idata)d %(imes)s, %(iany)d to %(fdia)s %(fdata)d %(fmes)s, %(fany)d')

        return dstr % { 'idia': _(self.data_inici.strftime('%A').decode('utf-8')),
                        'idata': self.data_inici.day,
                        'imes': _(self.data_inici.strftime('%B').decode('utf-8')),
                        'iany': self.data_inici.year,
                        'fdia': _(self.data_finalizacio.strftime('%A').decode('utf-8')),
                        'fdata': self.data_finalizacio.day,
                        'fmes': _(self.data_finalizacio.strftime('%B').decode('utf-8')),
                        'fany': self.data_finalizacio.year, }

    def is_owned_by(self, user):
        membre = user.get_profile()
        if membre in self.organitzadors.all():
            return True
        else:
            return False

    def organitzadors_html(self):
        return persones_html(list(self.organitzadors.all()) + persones_nom_cognoms(self.altres_organitzadors))

    def calendari_definit(self):
        items = sum([dia.items_programa.count() for dia in self.dies.all()])
        if items > 0:
            return True
        else:
            return False

    def save(self, *args, **kwargs):
        super(Seminari, self).save(*args, **kwargs)

        data = self.data_inici
        while data <= self.data_finalizacio:
            if self.dies.filter(data=data).count() == 0:
                nou_dia = self.dies.create(data=data)
            data += datetime.timedelta(days=1)


class Tema(TranslatableModel):
    seminari = models.ForeignKey(Seminari, verbose_name=_('seminar'),
                                 related_name='temes')
    ordre = models.IntegerField(_('order'), default=0)
    organitzadors = models.ManyToManyField(Membre, verbose_name=_('organisers'),
                                          related_name='temes',
                                          blank=True)
    altres_organitzadors = models.CharField(_('other organisers'),
                                            max_length=250, blank=True,
                                            null=True)
    publicacio = models.ForeignKey(Publicacio, verbose_name=_('publication'),
                                   related_name='temes',
                                   blank=True, null=True)
    referencies = models.TextField(_('references'), blank=True, null=True)

    translations = TranslatedFields(
        titol = models.CharField(_('title'), max_length=255),
        descripcio = models.TextField(_('description'), blank=True, null=True),
    )

    class Meta:
        verbose_name = _('theme')
        verbose_name_plural = _('themes')
        ordering = ['seminari', 'ordre']

    def __unicode__(self):
        return '%s (%s)' % (self.titol, self.seminari.nom,)
    
    @permalink
    def get_absolute_url(self):
        return ('seminari-tema-detall', (), {'tema_id': self.pk,
            'seminari_slug': self.seminari.slug})
    
    def is_owned_by(self, user):
        owned_by = False
        membre = user.get_profile()
        if membre in self.organitzadors.all():
            owned_by = True
        elif self.seminari.is_owned_by(user):
            owned_by = True
        return owned_by

    def organitzadors_html(self):
        return persones_html(list(self.organitzadors.all()) + persones_nom_cognoms(self.altres_organitzadors))


class Dia(TranslatableModel):
    data = models.DateField(_('date'))
    seminari = models.ForeignKey(Seminari, verbose_name=_('seminar'),
                                 related_name='dies')

    translations = TranslatedFields()

    class Meta:
        verbose_name = _('day')
        verbose_name_plural = _('days')
        ordering = ['seminari__data_inici', 'data',]

    def __unicode__(self):
        return _(self.data.strftime('%A').decode('utf-8')) + ' ' + unicode(self.data.day)
        #return str(self.data.day)

    def modifica_seminari(self):
        admin_url = reverse('admin:seminaris_seminari_change',
                            args=(self.seminari.pk,))
        return '<a href="%s">%s</a>' % (admin_url, self.seminari,)
    modifica_seminari.allow_tags = True


def nom_fitxer(ruta, nom):
    fitxer_nom = text_sense_accents(nom)
    return os.path.join(ruta, fitxer_nom)

def presentacio_nom_fitxer(xerrada, nom):
    ruta = 'xerrades/presentacions'
    fitxer_nom = nom_fitxer(ruta, nom)
    return fitxer_nom

def article_nom_fitxer(xerrada, nom):
    ruta = 'xerrades/articles'
    fitxer_nom = nom_fitxer(ruta, nom)
    return fitxer_nom

class Xerrada(TranslatableModel):
    tema = models.ForeignKey(Tema, verbose_name=_('theme'),
                             related_name='xerrades',
                             blank=True, null=True)
    ordre = models.IntegerField(_('order'), default=0)
    presentadors = models.ManyToManyField(Membre, verbose_name=_('presenters'),
                                          related_name='xerrades',
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
    )

    class Meta:
        verbose_name = _('talk')
        verbose_name_plural = _('talks')
        ordering = ['tema', 'ordre']

    def __unicode__(self):
        return self.titol

    @permalink
    def get_absolute_url(self):
        return ('seminari-xerrada-detall', (), {'xerrada_id': self.pk,
            'seminari_slug': self.seminari().slug})

    def seminari(self):
        seminari = None
        if self.tema:
            seminari = self.tema.seminari
        elif len(self.items_programa.all()) > 0:
            seminari = self.items_programa.all()[0].seminari()
        return seminari
    seminari.allow_tags = True

    def is_owned_by(self, user):
        owned_by = False
        membre = user.get_profile()
        if membre in self.presentadors.all():
            owned_by = True
        elif self.tema is not None and self.tema.is_owned_by(user):
            owned_by = True
        return owned_by

    def tots_presentadors(self):
        return persones_text(list(self.presentadors.all()) + persones_nom_cognoms(self.altres_presentadors))

    def presentadors_html(self):
        return persones_html(list(self.presentadors.all()) + persones_nom_cognoms(self.altres_presentadors))


class ItemPrograma(TranslatableModel):
    xerrada = models.ForeignKey(Xerrada, verbose_name=_('talk'),
                                related_name='items_programa',
                                blank=True, null=True)
    dia = models.ForeignKey(Dia, verbose_name=_('day'),
                            related_name='items_programa')
    hora_inici = models.TimeField(_('start time'))
    hora_finalizacio = models.TimeField(_('end time'))

    translations = TranslatedFields(
        descripcio = models.CharField(_('description'),
                                      max_length=255, blank=True, null=True,
            help_text=_("Only necessary if a talk isn't chosen.")),
    )

    class Meta:
        verbose_name = _('programme item')
        verbose_name_plural = _('programme items')
        ordering = ['dia', 'hora_inici']

    def __unicode__(self):
        duracio = self.duracio()
        if duracio:
            return '%s (%s): %s' % (unicode(self.dia), duracio, self.titol(),)
        else:
            return '<ItemPrograma>'

    def seminari(self):
        return self.dia.seminari
    seminari.allow_tags = True

    def titol(self):
        if self.xerrada is not None:
            return self.xerrada.titol
        else:
            return self.descripcio

    def duracio(self):
        duracio = None
        if self.hora_inici and self.hora_finalizacio:
            duracio = '%s - %s' % (self.hora_inici.strftime('%H.%M'),
                                   self.hora_finalizacio.strftime('%H.%M'),)
        return duracio

