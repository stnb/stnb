# -*- coding: utf-8 -*-
"""
Tests for the noticies (news) app.
"""
import datetime

from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from stnb.noticies.models import Noticia, MicroAlerta


class NoticiaModelTest(TestCase):
    """Tests for the Noticia (News) model."""

    def test_create_noticia(self):
        """Test creating a news item."""
        noticia = Noticia.objects.create(data=timezone.now())
        noticia.set_current_language('ca')
        noticia.titol = 'Important Announcement'
        noticia.descripcio = 'This is an important announcement.'
        noticia.save()
        self.assertEqual(noticia.titol, 'Important Announcement')

    def test_noticia_str(self):
        """Test string representation."""
        noticia = Noticia.objects.create(data=timezone.now())
        noticia.set_current_language('ca')
        noticia.titol = 'Test News'
        noticia.descripcio = 'Test description.'
        noticia.save()
        self.assertEqual(str(noticia), 'Test News')


class MicroAlertaModelTest(TestCase):
    """Tests for the MicroAlerta model."""

    def test_create_microalerta(self):
        """Test creating a microalert."""
        alerta = MicroAlerta.objects.create(data=timezone.now())
        alerta.set_current_language('ca')
        alerta.alerta = 'Registration is now open!'
        alerta.save()
        self.assertEqual(alerta.alerta, 'Registration is now open!')

    def test_microalerta_str(self):
        """Test string representation."""
        alerta = MicroAlerta.objects.create(data=timezone.now())
        alerta.set_current_language('ca')
        alerta.alerta = 'Test Alert'
        alerta.save()
        self.assertEqual(str(alerta), 'Test Alert')


class NoticiesViewTest(TestCase):
    """Tests for noticies views."""

    def setUp(self):
        self.client = Client()
        self.noticia = Noticia.objects.create(data=timezone.now())
        self.noticia.set_current_language('ca')
        self.noticia.titol = 'Test News Item'
        self.noticia.descripcio = 'This is a test news item.'
        self.noticia.save()

    def test_inici_view(self):
        """Test home page view returns 200."""
        response = self.client.get(reverse('inici'))
        self.assertEqual(response.status_code, 200)

    def test_noticies_ultimes_view(self):
        """Test recent news view returns 200."""
        response = self.client.get(reverse('noticies-ultimes'))
        self.assertEqual(response.status_code, 200)
