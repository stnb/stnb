# -*- coding: utf-8 -*-
"""
Tests for the pagines (flat pages) app.
"""
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from stnb.pagines.models import PaginaPlana


class PaginaPlanaModelTest(TestCase):
    """Tests for the PaginaPlana (Flat Page) model."""

    def test_create_pagina(self):
        """Test creating a flat page."""
        pagina = PaginaPlana.objects.create(slug='about-us')
        pagina.set_current_language('ca')
        pagina.titol = 'About Us'
        pagina.descripcio = 'Information about our organization.'
        pagina.save()
        self.assertEqual(pagina.slug, 'about-us')
        self.assertEqual(pagina.titol, 'About Us')

    def test_pagina_str(self):
        """Test string representation."""
        pagina = PaginaPlana.objects.create(slug='test-page')
        pagina.set_current_language('ca')
        pagina.titol = 'Test Page'
        pagina.descripcio = 'Test content.'
        pagina.save()
        self.assertEqual(str(pagina), 'Test Page')


class PaginaPlanaViewTest(TestCase):
    """Tests for pagina plana views."""

    def setUp(self):
        self.client = Client()
        self.pagina = PaginaPlana.objects.create(slug='sobre-stnb')
        self.pagina.set_current_language('ca')
        self.pagina.titol = 'About STNB'
        self.pagina.descripcio = 'Information about STNB.'
        self.pagina.save()

    def test_pagina_detail_view(self):
        """Test flat page detail view returns 200."""
        response = self.client.get(
            reverse('pagina-plana', kwargs={'slug': 'sobre-stnb'})
        )
        self.assertEqual(response.status_code, 200)
