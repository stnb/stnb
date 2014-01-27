# -*- coding: utf-8 -*-
from django.conf import settings

def get_all_language_codes():
    return [code for code, lang in settings.LANGUAGES]
