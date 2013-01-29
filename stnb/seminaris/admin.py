# -*- coding: utf-8 -*-
from django.contrib import admin
from hvad.admin import TranslatableAdmin, TranslatableStackedInline, TranslatableTabularInline
from tinymce.widgets import TinyMCE


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
    list_display = ('__unicode__', 'seminari',)
    #fields = ('seminari', 'translations__titol', 'order', 'organitzadors', 'translations__descripcio', 'referencies',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ['descripcio', 'referencies']:
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 20},
            ))
        return super(TemaAdmin, self).formfield_for_dbfield(db_field, **kwargs)

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
    list_display = ('__unicode__', 'tema', 'tots_presentadors', 'seminari',)
    list_filter = ('tema',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'abstracte':
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 20},
            ))
        return super(XerradaAdmin, self).formfield_for_dbfield(db_field, **kwargs)

class ItemProgramaAdmin(TranslatableAdmin):
    pass

admin.site.register(Seminari, SeminariAdmin)
admin.site.register(Tema, TemaAdmin)
admin.site.register(Dia, DiaAdmin)
admin.site.register(Xerrada, XerradaAdmin)
admin.site.register(ItemPrograma, ItemProgramaAdmin)

