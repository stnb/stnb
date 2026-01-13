# -*- coding: utf-8 -*-
"""
Tests for the seminaris (seminars) app.
"""
import datetime

from django.test import TestCase, Client
from django.urls import reverse

from stnb.comptes.models import Usuari
from stnb.membres.models import Membre
from stnb.seminaris.models import Seminari, Tema, Dia, Xerrada, ItemPrograma
from stnb.seminaris.utils import (
    persones_nom_cognoms, persona_html, persona_text,
    persones_html, persones_text
)


class SeminariModelTest(TestCase):
    """Tests for the Seminari (Seminar) model."""

    def test_create_seminari(self):
        """Test creating a basic seminar."""
        seminari = Seminari.objects.create(
            slug='test-seminar-2024',
            data_inici=datetime.date(2024, 6, 1),
            data_finalizacio=datetime.date(2024, 6, 5),
            actiu=True,
        )
        seminari.set_current_language('ca')
        seminari.nom = 'Test Seminar 2024'
        seminari.lloc = 'Barcelona'
        seminari.save()
        self.assertEqual(seminari.slug, 'test-seminar-2024')
        self.assertEqual(seminari.nom, 'Test Seminar 2024')
        self.assertTrue(seminari.actiu)

    def test_seminari_creates_days_on_save(self):
        """Test that saving a seminar creates Dia objects for each day."""
        seminari = Seminari.objects.create(
            slug='test-seminar',
            data_inici=datetime.date(2024, 6, 1),
            data_finalizacio=datetime.date(2024, 6, 3),
        )
        seminari.set_current_language('ca')
        seminari.nom = 'Test Seminar'
        seminari.lloc = 'Barcelona'
        seminari.save()
        self.assertEqual(seminari.dies.count(), 3)

    def test_seminari_str(self):
        """Test string representation of seminari."""
        seminari = Seminari.objects.create(
            slug='test-seminar',
            data_inici=datetime.date(2024, 6, 1),
            data_finalizacio=datetime.date(2024, 6, 3),
        )
        seminari.set_current_language('ca')
        seminari.nom = 'Test Seminar'
        seminari.lloc = 'Barcelona'
        seminari.save()
        self.assertEqual(str(seminari), 'Test Seminar')

    def test_calendari_definit_empty(self):
        """Test calendari_definit returns False when no items."""
        seminari = Seminari.objects.create(
            slug='test-seminar',
            data_inici=datetime.date(2024, 6, 1),
            data_finalizacio=datetime.date(2024, 6, 1),
        )
        seminari.set_current_language('ca')
        seminari.nom = 'Test Seminar'
        seminari.lloc = 'Barcelona'
        seminari.save()
        self.assertFalse(seminari.calendari_definit())


class SeminariUtilsTest(TestCase):
    """Tests for seminaris utility functions."""

    def test_persones_nom_cognoms_single(self):
        """Test parsing a single name."""
        result = persones_nom_cognoms('Joan Garcia')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['nom'], 'Joan')
        self.assertEqual(result[0]['cognoms'], 'Garcia')

    def test_persones_nom_cognoms_multiple(self):
        """Test parsing multiple names."""
        result = persones_nom_cognoms('Joan Garcia, Pere Martinez')
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['nom'], 'Joan')
        self.assertEqual(result[1]['nom'], 'Pere')

    def test_persones_nom_cognoms_empty(self):
        """Test parsing empty string."""
        result = persones_nom_cognoms('   ')
        self.assertEqual(result, [])

    def test_persones_nom_cognoms_compound_surname(self):
        """Test parsing compound surnames."""
        result = persones_nom_cognoms('Joan de la Cruz')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['nom'], 'Joan')
        self.assertEqual(result[0]['cognoms'], 'de la Cruz')

    def test_persona_text_dict(self):
        """Test persona_text with dictionary."""
        persona = {'nom': 'Joan', 'cognoms': 'Garcia'}
        self.assertEqual(persona_text(persona), 'Joan Garcia')

    def test_persones_text_single(self):
        """Test persones_text with single person."""
        persones = [{'nom': 'Joan', 'cognoms': 'Garcia'}]
        self.assertEqual(persones_text(persones), 'Joan Garcia')

    def test_persones_text_empty(self):
        """Test persones_text with empty list."""
        self.assertEqual(persones_text([]), '')


class SeminariViewTest(TestCase):
    """Tests for seminari views."""

    def setUp(self):
        self.client = Client()
        self.seminari = Seminari.objects.create(
            slug='test-seminar-2024',
            data_inici=datetime.date(2024, 6, 1),
            data_finalizacio=datetime.date(2024, 6, 3),
            actiu=True,
        )
        self.seminari.set_current_language('ca')
        self.seminari.nom = 'Test Seminar 2024'
        self.seminari.lloc = 'Barcelona'
        self.seminari.save()

    def test_seminari_list_view(self):
        """Test seminari list view returns 200."""
        response = self.client.get(reverse('seminari-llista'))
        self.assertEqual(response.status_code, 200)

    def test_seminari_detail_view(self):
        """Test seminari detail view returns 200."""
        response = self.client.get(
            reverse('seminari-detall', kwargs={'slug': self.seminari.slug})
        )
        self.assertEqual(response.status_code, 200)
