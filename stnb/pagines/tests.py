# -*- coding: utf-8 -*-
"""
Tests for the pagines (flat pages) app.
"""
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.utils import timezone

from stnb.pagines.models import PaginaPlana


class PaginaPlanaModelTest(TestCase):
    """Tests for the PaginaPlana (Flat Page) model."""

    def test_create_pagina(self):
        """Test creating a flat page."""
        pagina = PaginaPlana.objects.language('ca').create(
            slug='about-us',
            titol='About Us',
            descripcio='Information about our organization.',
        )
        self.assertEqual(pagina.slug, 'about-us')
        self.assertEqual(pagina.titol, 'About Us')

    def test_pagina_unicode(self):
        """Test unicode representation."""
        pagina = PaginaPlana.objects.language('ca').create(
            slug='test-page',
            titol='Test Page',
            descripcio='Test content.',
        )
        self.assertEqual(unicode(pagina), 'Test Page')

    def test_pagina_creat_auto(self):
        """Test that creat is set automatically."""
        before = timezone.now()
        pagina = PaginaPlana.objects.language('ca').create(
            slug='test-page',
            titol='Test Page',
            descripcio='Test content.',
        )
        after = timezone.now()
        self.assertGreaterEqual(pagina.creat, before)
        self.assertLessEqual(pagina.creat, after)

    def test_pagina_actualizat_auto(self):
        """Test that actualizat is updated on save."""
        pagina = PaginaPlana.objects.language('ca').create(
            slug='test-page',
            titol='Test Page',
            descripcio='Test content.',
        )
        original_update = pagina.actualizat

        pagina.titol = 'Updated Page'
        pagina.save()

        pagina = PaginaPlana.objects.language('ca').get(pk=pagina.pk)
        self.assertGreaterEqual(pagina.actualizat, original_update)

    def test_pagina_ordering(self):
        """Test that pages are ordered by slug."""
        pagina_b = PaginaPlana.objects.language('ca').create(
            slug='b-page',
            titol='B Page',
            descripcio='Content B.',
        )
        pagina_a = PaginaPlana.objects.language('ca').create(
            slug='a-page',
            titol='A Page',
            descripcio='Content A.',
        )
        pagines = list(PaginaPlana.objects.all())
        self.assertEqual(pagines[0].pk, pagina_a.pk)
        self.assertEqual(pagines[1].pk, pagina_b.pk)

    def test_pagina_with_translation(self):
        """Test flat page with translations."""
        pagina = PaginaPlana.objects.language('ca').create(
            slug='about',
            titol='Sobre',
            descripcio='Sobre el nostre seminari.',
        )
        pagina.translate('es')
        pagina.titol = 'Acerca de'
        pagina.descripcio = 'Acerca de nuestro seminario.'
        pagina.save()

        pagina_ca = PaginaPlana.objects.language('ca').get(pk=pagina.pk)
        self.assertEqual(pagina_ca.titol, 'Sobre')

        pagina_es = PaginaPlana.objects.language('es').get(pk=pagina.pk)
        self.assertEqual(pagina_es.titol, 'Acerca de')


class PaginaPlanaViewTest(TestCase):
    """Tests for pagina plana views."""

    def setUp(self):
        self.client = Client()
        self.pagina = PaginaPlana.objects.language('ca').create(
            slug='sobre-stnb',
            titol='About STNB',
            descripcio='Information about STNB.',
        )

    def test_pagina_detail_view(self):
        """Test flat page detail view returns 200."""
        response = self.client.get(
            reverse('pagina-plana', kwargs={'slug': 'sobre-stnb'})
        )
        self.assertEqual(response.status_code, 200)

    def test_pagina_detail_contains_title(self):
        """Test detail view contains page title."""
        response = self.client.get(
            reverse('pagina-plana', kwargs={'slug': 'sobre-stnb'})
        )
        self.assertContains(response, 'About STNB')

