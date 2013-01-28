# -*- coding: utf-8 -*-
import re
import datetime

from django.db import models
from django.db.models import permalink
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from hvad.models import TranslatableModel, TranslatedFields

from .utils import persones_nom_cognoms, persones_html
from stnb.membres.models import Membre
from stnb.membres.utils import cognoms_lexic

class Seminari(TranslatableModel):
    slug = models.SlugField(max_length=50)
    data_inici = models.DateField()
    data_finalizacio = models.DateField()
    organitzadors = models.ManyToManyField(Membre, related_name='seminaris',
                                           blank=True, null=True)
    altres_organitzadors = models.CharField(max_length=250, blank=True,
                                            null=True)
    programa_pdf = models.FileField(upload_to='seminaris/programes',
                                     blank=True, null=True)
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
                dstr= _('%(idia)s %(idata)d to %(fdia)s %(fdata)d %(imes)s, %(iany)d')
            else:
                dstr= _('%(idia)s %(idata)d %(imes)s to %(fdia)s %(fdata)d %(fmes)s, %(iany)d')
        else:
            dstr= _('%(idia)s %(idata)d %(imes)s, %(iany)s %(fdata)d to %(fdia)d %(fmes)s, %(fany)d')

        return dstr % { 'idia': _(self.data_inici.strftime('%A').decode('utf-8')),
                        'idata': self.data_inici.day,
                        'imes': _(self.data_inici.strftime('%B').decode('utf-8')),
                        'iany': self.data_inici.year,
                        'fdia': _(self.data_finalizacio.strftime('%A').decode('utf-8')),
                        'fdata': self.data_finalizacio.day,
                        'fmes': _(self.data_finalizacio.strftime('%B').decode('utf-8')),
                        'fany': self.data_finalizacio.year, }

    def organitzadors_html(self):
        return persones_html(list(self.organitzadors.all()) + persones_nom_cognoms(self.altres_organitzadors))

    def presentadors_comunicacions_html(self):
        items = ItemPrograma.objects.filter(dia__in=self.dies.all(), xerrada__isnull=False, xerrada__tema__isnull=True).distinct()
        p_dict = {}
        for xerrada in [i.xerrada for i in items]:
            for p in xerrada.tots_presentadors():
                if isinstance(p, dict):
                    nom_cognoms = p['nom'] + ' ' + p['cognoms']
                else:
                    nom_cognoms = p.nom + ' ' + p.cognoms
                p_dict[nom_cognoms] = p
        return persones_html(p_dict.values())


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
    altres_organitzadors = models.CharField(max_length=250, blank=True,
                                            null=True)
    referencies = models.TextField(blank=True, null=True)

    translations = TranslatedFields(
        titol = models.CharField(max_length=255),
        descripcio = models.TextField(blank=True, null=True),
    )

    class Meta:
        verbose_name_plural = 'temes'
        ordering = ['seminari', 'ordre']

    def __unicode__(self):
        return '%s (%s)' % (self.titol, self.seminari.nom,)
    
    @permalink
    def get_absolute_url(self):
        return ('seminari-tema-detall', (), {'tema_id': self.pk,
            'seminari_slug': self.seminari.slug})
    
    def organitzadors_html(self):
        print list(self.organitzadors.all()) + persones_nom_cognoms(self.altres_organitzadors)
        return persones_html(list(self.organitzadors.all()) + persones_nom_cognoms(self.altres_organitzadors))


class Dia(TranslatableModel):
    data = models.DateField()
    seminari = models.ForeignKey(Seminari, related_name='dies')

    translations = TranslatedFields()

    class Meta:
        verbose_name_plural = 'dies'
        ordering = ['seminari__data_inici', 'data',]

    def __unicode__(self):
        return _(self.data.strftime('%A').decode('utf-8')) + ' ' + unicode(self.data.day)
        #return str(self.data.day)

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
    altres_presentadors = models.CharField(max_length=250, blank=True,
                                           null=True)

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

    def presentadors_html(self):
        return persones_html(list(self.presentadors.all()) + persones_nom_cognoms(self.altres_presentadors))


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

