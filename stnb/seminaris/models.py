# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.db.models import permalink
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from hvad.models import TranslatableModel, TranslatedFields

from stnb.membres.models import Membre

class Seminari(TranslatableModel):
    slug = models.SlugField(max_length=50)
    data_inici = models.DateField()
    organitzadors = models.ManyToManyField(Membre, related_name='seminaris')
    data_finalizacio = models.DateField()
    actiu = models.BooleanField(default=False)
    
    translations = TranslatedFields(
        nom = models.CharField(max_length=50),
        lloc = models.TextField(),
    )

    class Meta:
        verbose_name_plural = 'seminaris'
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
                dstr= _('%(idia)s %(idata)d to %(fdia)s %(fdata)d of %(imes)s, %(iany)d')
            else:
                dstr= _('%(idia)s %(idata)d of %(fmes)s to %(fdia)s %(fdata)d of %(fmes)s, %(iany)d')
        else:
            dstr= _('%(idia)s %(idata)d of %(imes)s, %(iany)s %(fdata)d to %(fdia)d of %(fmes)s, %(fany)d')

        return dstr % { 'idia': _(self.data_inici.strftime('%A')),
                        'idata': self.data_inici.day,
                        'imes': _(self.data_inici.strftime('%B')),
                        'iany': self.data_inici.year,
                        'fdia': _(self.data_finalizacio.strftime('%A')),
                        'fdata': self.data_finalizacio.day,
                        'fmes': _(self.data_finalizacio.strftime('%B')),
                        'fany': self.data_finalizacio.year, }

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
    seminari = models.ForeignKey(Seminari, related_name='temes')
    ordre = models.IntegerField(default=0)
    organitzadors = models.ManyToManyField(Membre, related_name='temes',
                                          blank=True, null=True)

    translations = TranslatedFields(
        titol = models.CharField(max_length=255),
        descripcio = models.TextField(blank=True, null=True),
    )

    class Meta:
        verbose_name_plural = 'temes'
        ordering = ['seminari', 'ordre']

    def __unicode__(self):
        return self.titol

class Dia(TranslatableModel):
    data = models.DateField()
    seminari = models.ForeignKey(Seminari, related_name='dies')

    translations = TranslatedFields()

    class Meta:
        verbose_name_plural = 'dies'
        ordering = ['seminari__data_inici', 'data',]

    def __unicode__(self):
        return '%s %d' % (_(self.data.strftime('%A')), self.data.day,)

    def modifica_seminari(self):
        admin_url = reverse('admin:seminaris_seminari_change',
                            args=(self.seminari.pk,))
        return '<a href="%s">%s</a>' % (admin_url, self.seminari,)
    modifica_seminari.allow_tags = True

class Xerrada(TranslatableModel):
    tema = models.ForeignKey(Tema, related_name='xerrades',
                               blank=True, null=True)
    ordre = models.IntegerField(default=0)
    presentadors = models.ManyToManyField(Membre, related_name='xerrades',
                                          blank=True, null=True)
    altres_presentadors = models.CharField(max_length=100, blank=True, null=True)

    presentacio = models.FileField(upload_to='xerrades/presentacions',
                                   blank=True, null=True)
    article = models.FileField(upload_to='xerrades/articles',
                               blank=True, null=True)

    translations = TranslatedFields(
        titol = models.CharField(max_length=255),
        abstracte = models.TextField(blank=True, null=True),
    )

    class Meta:
        verbose_name_plural = 'xerrades'
        ordering = ['tema', 'ordre']

    def __unicode__(self):
        return self.titol

    def seminari(self):
        return self.tema.seminari
    seminari.allow_tags = True

    def presentadors_html(self):
        return self.altres_presentadors

class ItemPrograma(TranslatableModel):
    xerrada = models.ForeignKey(Xerrada, related_name='items_programa',
                                  blank=True, null=True)
    dia = models.ForeignKey(Dia, related_name='items_programa')
    hora_inici = models.TimeField()
    hora_finalizacio = models.TimeField()

    translations = TranslatedFields(
        descripcio = models.CharField(help_text=_("Only necessary if a talk isn't chosen."),
                                      max_length=255, blank=True, null=True),
    )

    class Meta:
        verbose_name = 'ìtem del programa'
        verbose_name_plural = 'ìtems del programa'
        ordering = ['dia', 'hora_inici']

    def __unicode__(self):
        duracio = self.duracio()
        if duracio:
            return '%s (%s): %s' % (self.dia, duracio, self.titol(),)
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

