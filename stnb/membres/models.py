# -*- coding: utf-8 -*-
import os
import re
import uuid
import unicodedata

from django.conf import settings
from django.db import models
from django.db import IntegrityError
from django.urls import reverse
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

from .utils import crear_imagen_petita
from stnb.institucions.models import Institucio

class Membre(TranslatableModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nom = models.CharField(_('name'), max_length=50, null=True)
    cognoms = models.CharField(_('surname'), max_length=100, null=True)
    slug = models.SlugField(max_length=160, unique=True, blank=True)
    afiliacio = models.ForeignKey(Institucio, verbose_name=_('affiliation'),
                                  related_name='membres', blank=True, null=True,
                                  on_delete=models.SET_NULL)
    foto = models.ImageField(_('photo'), upload_to='membres/fotos/',
                             blank=True, null=True)
    enllac = models.CharField(_('link'), max_length=250, blank=True, null=True)
    membre_des_de = models.IntegerField(_('member since'),
                                        blank=True, null=True)
    membre_actual = models.BooleanField(_('current member'), default=True)
    amagar_perfil = models.BooleanField(_('hide profile'), default=False)

    translations = TranslatedFields(
        text = models.TextField(_('biography'), blank=True, null=True),
    )

    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')
        ordering = ['cognoms', 'nom']

    def __str__(self):
        nom_complet = self.nom_complet()
        if nom_complet:
            return nom_complet
        else:
            return str(_('unnamed'))

    def get_absolute_url(self):
        return reverse('membre-detall', kwargs={'slug': self.slug})

    def slug_de_nom_complet(self):
        nom_complet = self.nom_complet()
        if nom_complet:
            nfd_nom = ''.join((c for c in unicodedata.normalize('NFD', nom_complet) if unicodedata.category(c) != 'Mn'))
            return re.sub(r'[^\w\-]+', '-', nfd_nom).lower()
        else:
            return ''

    def save(self, *args, **kwargs):
        nom_complet = self.nom_complet()
        if nom_complet:
            self.slug = self.slug_de_nom_complet()
        elif not self.slug:
            self.slug = str(uuid.uuid4())
        try:
            obj = super(Membre, self).save(*args, **kwargs)
        except IntegrityError as e:
            if nom_complet:
                self.slug = re.sub(r'\s', '-', self.slug_de_nom_complet()+'-'+str(uuid.uuid4())[0:4]).lower()
                obj = super(Membre, self).save(*args, **kwargs)
            else:
                raise e

        if self.foto:
            self.crear_totes_fotos()

        return obj

    def nom_complet(self):
        if self.nom or self.cognoms:
            if self.nom and self.cognoms:
                return '%s %s' % (self.nom, self.cognoms,)
            elif self.nom:
                return self.nom
            elif self.cognoms:
                return self.cognoms
        else:
            return None

    def enllac_a(self):
        enllac_a = self.enllac
        if enllac_a is not None:
            if not re.match(r'^https?:\/\/', enllac_a):
                enllac_a = 'http://' + enllac_a
        return enllac_a

    def text_qualsevol_llengua(self):
        text = self.text
        if text is None or len(text) == 0:
            for code in [t[0] for t in settings.LANGUAGES]:
                text = Membre.objects.language(code).get(pk=self.id).text
                if text is not None and len(text) > 0:
                    break
        return text

    def crear_foto_petita(self):
        path_complet = os.path.join(settings.MEDIA_ROOT, str(self.foto))
        crear_imagen_petita(path_complet, self.foto_petita(), 200)

    def foto_petita(self):
        base, ext = os.path.splitext(str(self.foto))
        return '%s-thumbnail.png' % (base,)

    def crear_foto_llista(self):
        path_complet = os.path.join(settings.MEDIA_ROOT, str(self.foto))
        crear_imagen_petita(path_complet, self.foto_llista(), 100)

    def foto_llista(self):
        base, ext = os.path.splitext(str(self.foto))
        return '%s-llista.png' % (base,)

    def crear_totes_fotos(self):
        self.crear_foto_petita()
        self.crear_foto_llista()


def user_post_save(sender, instance, created, *args, **kwargs):
    # Crear un nou modell Membre
    if created:
        nou_membre = Membre.objects.create(user=instance)
        nou_membre.save()
