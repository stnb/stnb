# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from stnb.comptes.models import Usuari

def create_user(email, password, **extra_fields):
    return Usuari.objects.create_user(email, password, **extra_fields)
