# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from hvad.models import TranslatableModel, TranslatedFields

class Seminari(TranslatableModel):
    nom = models.CharField(max_length=50)
    data_inici = models.DateField()
    data_finalizacio = models.DateField()
    actiu = models.BooleanField(default=False)
    
    translations = TranslatedFields(
        lloc = models.TextField(),
    )

    def __unicode__(self):
        return self.nom

    def save(self, *args, **kwargs):
        super(Seminari, self).save(*args, **kwargs)

        data = self.data_inici
        while data <= self.data_finalizacio:
            if self.dies.filter(data=data).count() == 0:
                nou_dia = self.dies.create(data=data)
            data += datetime.timedelta(days=1)


class Tema(TranslatableModel):
    seminari = models.ForeignKey(Seminari, related_name='temes')

    translations = TranslatedFields(
        nom = models.CharField(max_length=255),
        descripcio = models.TextField(),
    )

    class Meta:
        verbose_name_plural = 'temes'

    def __unicode__(self):
        return self.nom

class Dia(TranslatableModel):
    data = models.DateField()
    seminari = models.ForeignKey(Seminari, related_name='dies')

    translations = TranslatedFields()

    class Meta:
        verbose_name_plural = 'dies'

    def __unicode__(self):
        return self.data.strftime('%A ') + unicode(self.data.day)

    def modifica_seminari(self):
        admin_url = reverse('admin:seminaris_seminari_change',
                            args=(self.seminari.pk,))
        return '<a href="%s">%s</a>' % (admin_url, self.seminari,)
    modifica_seminari.allow_tags = True

class Xerrada(TranslatableModel):
    tema = models.ForeignKey(Tema, related_name='xerrades',
                               blank=True, null=True)
    presentadors = models.ManyToManyField(User, related_name='xerrades',
                                          blank=True, null=True)
    altre_presentadors = models.CharField(max_length=100, blank=True, null=True)

    presentacio = models.FileField(upload_to='presentacions',
                                   blank=True, null=True)
    article = models.FileField(upload_to='articles', blank=True, null=True)

    translations = TranslatedFields(
        nom = models.CharField(max_length=255),
        descripcio = models.TextField(),
    )

    class Meta:
        verbose_name_plural = 'xerrades'

    def __unicode__(self):
        return self.nom

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

    def __unicode__(self):
        duracio = self.duracio()
        if duracio:
            return duracio
        else:
            return '<ItemPrograma>'

    def duracio(self):
        duracio = None
        if self.hora_inici and self.hora_finalizacio:
            duracio = '%s - %s' % (self.hora_inici.strftime('%H.%M'),
                                   self.hora_finalizacio.strftime('%H.%M'),)
        return duracio

