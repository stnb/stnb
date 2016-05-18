# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from stnb.comptes.managers import UsuariGerent

class Usuari(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email'), unique=True)
    nom = models.CharField(_('name'), max_length=50, null=True)
    cognoms = models.CharField(_('surname'), max_length=100, null=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        )
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as '
            'active. Unselect this instead of deleting accounts.'
        )
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UsuariGerent()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        swappable = 'AUTH_USER_MODEL'

    @property
    def username(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def get_profile(self):
        from stnb.membres.models import Membre
        try:
            membre = Membre.objects.get(user=self)
        except Membre.NotFound as e:
            membre = None
        return membre
