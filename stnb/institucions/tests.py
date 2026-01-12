# -*- coding: utf-8 -*-
"""
Tests for the institucions (institutions) app.
"""
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from stnb.institucions.models import Institucio


class InstitucioModelTest(TestCase):
    """Tests for the Institucio (Institution) model."""

    def test_create_institucio(self):
        """Test creating a basic institution."""
        inst = Institucio.objects.language('ca').create(
            nom='University of Barcelona',
            nom_curt='UB',
            url='http://www.ub.edu',
            descripcio='A major university in Barcelona.',
        )
        self.assertEqual(inst.nom, 'University of Barcelona')
        self.assertEqual(inst.nom_curt, 'UB')
        self.assertEqual(inst.url, 'http://www.ub.edu')

    def test_unicode_representation(self):
        """Test unicode representation returns uppercase short name."""
        inst = Institucio.objects.language('ca').create(
            nom='University of Barcelona',
            nom_curt='ub',
            url='http://www.ub.edu',
            descripcio='A major university.',
        )
        self.assertEqual(unicode(inst), 'UB')

    def test_institucio_with_translation(self):
        """Test institution with translation fields."""
        inst = Institucio.objects.language('ca').create(
            nom='Universitat de Barcelona',
            nom_curt='UB',
            url='http://www.ub.edu',
            descripcio='Una universitat a Barcelona.',
        )
        self.assertEqual(inst.descripcio, 'Una universitat a Barcelona.')

    def test_multiple_translations(self):
        """Test institution with multiple language translations."""
        inst = Institucio.objects.language('ca').create(
            nom='Universitat de Barcelona',
            nom_curt='UB',
            url='http://www.ub.edu',
            descripcio='Una universitat a Barcelona.',
        )
        inst.translate('es')
        inst.descripcio = 'Una universidad en Barcelona.'
        inst.save()

        inst_ca = Institucio.objects.language('ca').get(pk=inst.pk)
        self.assertEqual(inst_ca.descripcio, 'Una universitat a Barcelona.')

        inst_es = Institucio.objects.language('es').get(pk=inst.pk)
        self.assertEqual(inst_es.descripcio, 'Una universidad en Barcelona.')


class InstitucioViewTest(TestCase):
    """Tests for institucio views."""

    def setUp(self):
        self.client = Client()
        self.institucio = Institucio.objects.language('ca').create(
            nom='Test University',
            nom_curt='TU',
            url='http://test.edu',
            descripcio='A test institution.',
        )

    def test_institucio_list_view(self):
        """Test institucio list view returns 200."""
        response = self.client.get(reverse('institucio-llista'))
        self.assertEqual(response.status_code, 200)
