# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Usuari

class UsuariAdmin(admin.ModelAdmin):
    model = Usuari
    search_fields = ('nom', 'cognoms', 'email')
    ordering = ('cognoms',)
    list_display = ('email', 'nom', 'cognoms', 'is_staff',
                    'is_active', 'date_joined')

admin.site.register(Usuari, UsuariAdmin)


