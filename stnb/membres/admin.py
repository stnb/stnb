# -*- coding: utf-8 -*-
from django.contrib import admin
from hvad.admin import TranslatableAdmin

from .models import Membre

class MembreAdmin(TranslatableAdmin):
    model = Membre
    list_display = ('nom_complet', 'membre_des_de', 'afiliacio',
                    'membre_actual', 'amagar_perfil')

admin.site.register(Membre, MembreAdmin)

