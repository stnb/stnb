# -*- coding: utf-8 -*-
from django.contrib import admin
from hvad.admin import TranslatableAdmin

from .models import Institucio

class InstitucioAdmin(TranslatableAdmin):
    pass

admin.site.register(Institucio, InstitucioAdmin)


