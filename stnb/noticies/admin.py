# -*- coding: utf-8 -*-
from django.contrib import admin
from hvad.admin import TranslatableAdmin, TranslatableStackedInline, TranslatableTabularInline


from .models import Noticia, MicroAlerta

class NoticiaAdmin(TranslatableAdmin):
    model = Noticia
    pass

class MicroAlertaAdmin(TranslatableAdmin):
    model = MicroAlerta
    pass


admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(MicroAlerta, MicroAlertaAdmin)


