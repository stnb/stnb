# -*- coding: utf-8 -*-
"""
Base test utilities and helper functions for the STNB test suite.
"""
import datetime

from django.test import TestCase, Client
from django.conf import settings

from stnb.comptes.models import Usuari
from stnb.institucions.models import Institucio
from stnb.membres.models import Membre


class BaseTestCase(TestCase):
    """Base test case with common helper methods."""

    def setUp(self):
        self.client = Client()

    def create_user(self, email='test@example.com', password='testpass123',
                    nom='Test', cognoms='User', is_staff=False, is_superuser=False):
        """Create a test user."""
        user = Usuari.objects.create_user(email=email, password=password)
        user.nom = nom
        user.cognoms = cognoms
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        return user

    def create_institucio(self, nom='Test University', nom_curt='TU',
                          url='http://test.edu', descripcio='A test institution'):
        """Create a test institution."""
        inst = Institucio.objects.create(
            nom=nom,
            nom_curt=nom_curt,
            url=url,
        )
        inst.set_current_language('ca')
        inst.descripcio = descripcio
        inst.save()
        return inst

    def create_membre(self, user=None, nom='Test', cognoms='Member',
                      membre_actual=True, amagar_perfil=False):
        """Create a test member."""
        if user is None:
            user = self.create_user(
                email='%s.%s@example.com' % (nom.lower(), cognoms.lower())
            )
        membre = Membre.objects.create(
            user=user,
            nom=nom,
            cognoms=cognoms,
            membre_actual=membre_actual,
            amagar_perfil=amagar_perfil,
        )
        return membre

    def login(self, user=None, email='test@example.com', password='testpass123'):
        """Login a user for authenticated tests."""
        if user is None:
            user = self.create_user(email=email, password=password)
        self.client.login(username=email, password=password)
        return user
