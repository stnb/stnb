# -*- coding: utf-8 -*-
import os

from django.db import models
from django.utils.translation import ugettext_lazy as _
from hvad.models import TranslatableModel, TranslatedFields

from stnb.membres.models import Membre
from stnb.seminaris.utils import persones_nom_cognoms, persones_html, \
                                 persones_text
from stnb.membres.utils import cognoms_lexic
from stnb.utils.text_processing import text_sense_accents

def nom_fitxer(ruta, nom):
    fitxer_nom = text_sense_accents(nom)
    return os.path.join(ruta, fitxer_nom)

def publicacio_nom_fitxer(xerrada, nom):
    ruta = 'publicacions/publicacions'
    fitxer_nom = nom_fitxer(ruta, nom)
    return fitxer_nom

class Publicacio(TranslatableModel):
    autors = models.ManyToManyField(Membre, verbose_name=_('authors'),
                                    related_name='publicacions',
                                    blank=True)
    altres_autors = models.CharField(_('other authors'), max_length=250,
                                     blank=True, null=True)
    editors = models.ManyToManyField(Membre, verbose_name=_('editors'),
                                     related_name='publicacions_editades',
                                     blank=True)
    altres_editors = models.CharField(_('other editors'), max_length=250,
                                      blank=True, null=True)
    isbn = models.CharField('ISBN', max_length=20, blank=True, null=True)
    data_publicacio = models.DateField(_('publication date'),
            help_text=_('Only the month and year are displayed'),
            blank=True, null=True)
    fitxer = models.FileField(_('file'), upload_to=publicacio_nom_fitxer,
                               blank=True, null=True)

    translations = TranslatedFields(
        nom = models.CharField(_('name'), help_text=_('Publication name'),
                               max_length=128),
        descripcio = models.CharField(_('description'), max_length=255,
                                      help_text=_('A short description.'),
                                      blank=True, null=True),
    )

    class Meta:
        verbose_name = _('publication')
        verbose_name_plural = _('publicacions')
        ordering = ['data_publicacio',]

    def __unicode__(self):
        return self.nom

    def mes_any_publicacio(self):
        return _(self.data_publicacio.strftime('%B').decode('utf-8')) + ' ' + unicode(self.data_publicacio.year)

    def nom_fitxer(self):
        return os.path.basename(self.fitxer.name)

    def autors_html(self):
        return persones_html(list(self.autors.all()) + persones_nom_cognoms(self.altres_autors))

    def editors_html(self):
        return persones_html(list(self.editors.all()) + persones_nom_cognoms(self.altres_editors))


