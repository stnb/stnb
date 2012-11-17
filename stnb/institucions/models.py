# -*- coding: utf-8 -*-
from django.db import models
from hvad.models import TranslatableModel, TranslatedFields

class Institucio(TranslatableModel):
    nom = models.CharField(max_length=50)
    nom_curt = models.SlugField(max_length=10)
    url = models.CharField(max_length=100)

    translations = TranslatedFields(
        descripcio = models.TextField(),
    )

    def __unicode__(self):
        return self.nom_curt.upper()
