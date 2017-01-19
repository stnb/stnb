# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext as _
from hvad.admin import TranslatableAdmin, TranslatableStackedInline
from tinymce.widgets import TinyMCE

from .models import Serie, Esdeveniment

class EsdevenimentAdmin(TranslatableAdmin):
    list_display = ('__unicode__', 'data', 'serie',)
    readonly_fields = ('slug',)
    filter_horizontal = ['amfitrions', 'presentadors']

class EsdevenimnetInline(TranslatableStackedInline):
    model = Esdeveniment
    readonly_fields = ('slug',)
    filter_horizontal = ['amfitrions', 'presentadors']
    extra = 1

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ['abstracte']:
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 20},
            ))
        return super(EsdevenimnetInline, self)\
                .formfield_for_dbfield(db_field, **kwargs)

class SerieAdmin(TranslatableAdmin):
    list_display = ('__unicode__', 'nombre_de_esdeveniments')
    readonly_fields = ('slug',)
    filter_horizontal = ['organitzadors']
    inlines = [
        EsdevenimnetInline,
    ]

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ['descripcio']:
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 20},
            ))
        return super(SerieAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Esdeveniment, EsdevenimentAdmin)
admin.site.register(Serie, SerieAdmin)
