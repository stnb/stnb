# -*- coding: utf-8 -*-
from django.contrib import admin
from hvad.admin import TranslatableAdmin
from tinymce.widgets import TinyMCE

from .models import PaginaPlana

class PaginaPlanaAdmin(TranslatableAdmin):
    model = PaginaPlana
    list_display = ('__unicode__', 'slug')

#    def formfield_for_dbfield(self, db_field, **kwargs):
#        if db_field.name == 'descripcio':
#            return db_field.formfield(widget=TinyMCE(
#                attrs={'cols': 80, 'rows': 20},
#            ))
#        return super(PaginaPlanaAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.register(PaginaPlana, PaginaPlanaAdmin)
