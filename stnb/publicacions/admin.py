# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext as _
from hvad.admin import TranslatableAdmin, TranslatableStackedInline, \
                       TranslatableTabularInline

from .models import Publicacio
from .forms import PublicacioNomFitxerForm

class PublicacioAdmin(TranslatableAdmin):
    form = PublicacioNomFitxerForm

admin.site.register(Publicacio, PublicacioAdmin)
