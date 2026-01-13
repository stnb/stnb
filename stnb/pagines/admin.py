# -*- coding: utf-8 -*-
from django.contrib import admin
from parler.admin import TranslatableAdmin
from tinymce.widgets import TinyMCE

from .models import PaginaPlana

class PaginaPlanaAdmin(TranslatableAdmin):
    model = PaginaPlana
    list_display = ('__str__', 'slug')


admin.site.register(PaginaPlana, PaginaPlanaAdmin)
