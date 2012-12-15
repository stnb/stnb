# -*- coding: utf-8 -*-
import datetime
import os
import re

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import permalink
from django.db.models import signals
from hvad.models import TranslatableModel, TranslatedFields

from stnb.institucions.models import Institucio

class Membre(TranslatableModel):
    user = models.ForeignKey(User, unique=True)
    nom = models.CharField(max_length=50, null=True)
    cognoms = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=160, unique=True, blank=True)
    afiliacio = models.ForeignKey(Institucio, related_name='membres',
                                  blank=True, null=True)
    foto = models.ImageField(upload_to='membres/fotos/', blank=True, null=True)
    membre_des_de = models.IntegerField(blank=True, null=True)
    membre_actual = models.BooleanField(default=True)

    translations = TranslatedFields(
        text = models.TextField(blank=True, null=True),
    )

    class Meta:
        ordering = ['cognoms', 'nom']

    def __unicode__(self):
        nom_complet = self.nom_complet()
        if nom_complet:
            return nom_complet
        else:
            return _('Unnamed')

    @permalink
    def get_absolute_url(self):
        return ('membre-detall', (), {'slug': self.slug})

    def save(self, *args, **kwargs):
        nom_complet = self.nom_complet()
        if nom_complet:
            self.slug = re.sub(r'\s', '-', nom_complet).lower()
        elif not self.slug:
            import uuid
            self.slug = uuid.uuid4()
        if self.foto:
            self.creat_foto_petita()
        return super(Membre, self).save(*args, **kwargs)

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

    def creat_foto_petita(self):
        from PIL import Image

        path_complet = os.path.join(settings.MEDIA_ROOT, unicode(self.foto))
        file, ext = os.path.splitext(path_complet)
        im = Image.open(path_complet)
        width = 200
        height = im.size[1] * width / im.size[0]
        im.thumbnail((width, height), Image.ANTIALIAS)
        im.save(os.path.join(settings.MEDIA_ROOT, self.foto_petita()), "PNG")

    def foto_petita(self):
        base, ext = os.path.splitext(unicode(self.foto))
        return '%s-thumbnail.png' % (base,)


def user_post_save(sender, instance, created, *args, **kwargs):
    # Crear un nou modell Membre
    if created:
        nou_membre = Membre.objects.create(user=instance)
        nou_membre.save()

signals.post_save.connect(user_post_save, sender=User,
                          dispatch_uid='crear_nou_membre')
#User.profile = property(lambda u: Membre.objects.get_or_create(user=u)[0])
