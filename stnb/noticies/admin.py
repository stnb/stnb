# -*- coding: utf-8 -*-
from django.contrib import admin
from hvad.admin import TranslatableAdmin
from tinymce.widgets import TinyMCE


from .models import Noticia, MicroAlerta

class NoticiaAdmin(TranslatableAdmin):
    model = Noticia
    list_display = ('__unicode__', 'data',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'descripcio':
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 100, 'rows': 20},
            ))
        return super(NoticiaAdmin, self).formfield_for_dbfield(db_field, **kwargs)

class MicroAlertaAdmin(TranslatableAdmin):
    model = MicroAlerta
    list_display = ('__unicode__', 'data',)


admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(MicroAlerta, MicroAlertaAdmin)


