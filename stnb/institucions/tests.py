# -*- coding: utf-8 -*-
"""
Tests for the institucions (institutions) app.
"""
from django.test import TestCase, Client
from django.urls import reverse

from stnb.institucions.models import Institucio


class InstitucioModelTest(TestCase):
    """Tests for the Institucio (Institution) model."""

    def test_create_institucio(self):
        """Test creating a basic institution."""
        inst = Institucio.objects.create(
            nom='University of Barcelona',
            nom_curt='UB',
            url='http://www.ub.edu',
        )
        inst.set_current_language('ca')
        inst.descripcio = 'A major university in Barcelona.'
        inst.save()
        self.assertEqual(inst.nom, 'University of Barcelona')
        self.assertEqual(inst.nom_curt, 'UB')
        self.assertEqual(inst.url, 'http://www.ub.edu')

    def test_str_representation(self):
        """Test string representation returns uppercase short name."""
        inst = Institucio.objects.create(
            nom='University of Barcelona',
            nom_curt='ub',
            url='http://www.ub.edu',
        )
        inst.set_current_language('ca')
        inst.descripcio = 'A major university.'
        inst.save()
        self.assertEqual(str(inst), 'UB')

    def test_institucio_with_translation(self):
        """Test institution with translation fields."""
        inst = Institucio.objects.create(
            nom='Universitat de Barcelona',
            nom_curt='UB',
            url='http://www.ub.edu',
        )
        inst.set_current_language('ca')
        inst.descripcio = 'Una universitat a Barcelona.'
        inst.save()
        self.assertEqual(inst.descripcio, 'Una universitat a Barcelona.')

    def test_multiple_translations(self):
        """Test institution with multiple language translations."""
        inst = Institucio.objects.create(
            nom='Universitat de Barcelona',
            nom_curt='UB',
            url='http://www.ub.edu',
        )
        inst.set_current_language('ca')
        inst.descripcio = 'Una universitat a Barcelona.'
        inst.save()

        inst.set_current_language('es')
        inst.descripcio = 'Una universidad en Barcelona.'
        inst.save()

        inst.set_current_language('ca')
        self.assertEqual(inst.descripcio, 'Una universitat a Barcelona.')

        inst.set_current_language('es')
        self.assertEqual(inst.descripcio, 'Una universidad en Barcelona.')


class InstitucioViewTest(TestCase):
    """Tests for institucio views."""

    def setUp(self):
        self.client = Client()
        self.institucio = Institucio.objects.create(
            nom='Test University',
            nom_curt='TU',
            url='http://test.edu',
        )
        self.institucio.set_current_language('ca')
        self.institucio.descripcio = 'A test institution.'
        self.institucio.save()

    def test_institucio_list_view(self):
        """Test institucio list view returns 200."""
        response = self.client.get(reverse('institucio-llista'))
        self.assertEqual(response.status_code, 200)
