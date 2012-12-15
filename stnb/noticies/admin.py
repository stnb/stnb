# -*- coding: utf-8 -*-
from django.contrib import admin
from hvad.admin import TranslatableAdmin, TranslatableStackedInline, TranslatableTabularInline


from .models import Noticia, MicroAlerta

class NoticiaAdmin(TranslatableAdmin):
    model = Noticia
    list_display = ('__unicode__', 'data',)

class MicroAlertaAdmin(TranslatableAdmin):
    model = MicroAlerta
    list_display = ('__unicode__', 'data',)


admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(MicroAlerta, MicroAlertaAdmin)


