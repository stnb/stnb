# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import gettext as _
from parler.admin import TranslatableAdmin, TranslatableStackedInline, \
                       TranslatableTabularInline

from .models import Publicacio
from .forms import PublicacioNomFitxerForm

class PublicacioAdmin(TranslatableAdmin):
    form = PublicacioNomFitxerForm

admin.site.register(Publicacio, PublicacioAdmin)
