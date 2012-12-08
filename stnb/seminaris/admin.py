# -*- coding: utf-8 -*-
from django.contrib import admin
from hvad.admin import TranslatableAdmin, TranslatableStackedInline, TranslatableTabularInline


from .models import Seminari, Tema, Dia, Xerrada, ItemPrograma

class TemaInline(TranslatableStackedInline):
    model = Tema

class XerradaInline(TranslatableStackedInline):
    model = Xerrada

class SeminariAdmin(TranslatableAdmin):
   inlines = [
        TemaInline,
    ]

class TemaAdmin(TranslatableAdmin):
    pass

class ItemProgramaInline(TranslatableTabularInline):
    model = ItemPrograma

class DiaAdmin(TranslatableAdmin):
    list_display = ('__unicode__', 'seminari',)
    list_filter = ('seminari',)
    fields = ('seminari', 'modifica_seminari', 'data',)
    readonly_fields = ('seminari', 'modifica_seminari', 'data',)

    inlines = [
        ItemProgramaInline,
    ]

class XerradaAdmin(TranslatableAdmin):
    list_display = ('__unicode__', 'tema', 'seminari',)
    list_filter = ('tema',)

class ItemProgramaAdmin(TranslatableAdmin):
    pass

admin.site.register(Seminari, SeminariAdmin)
admin.site.register(Tema, TemaAdmin)
admin.site.register(Dia, DiaAdmin)
admin.site.register(Xerrada, XerradaAdmin)
admin.site.register(ItemPrograma, ItemProgramaAdmin)

