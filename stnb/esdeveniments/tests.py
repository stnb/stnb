# -*- coding: utf-8 -*-
"""
Tests for the esdeveniments (events) app.
"""
import datetime

from django.test import TestCase, Client
from django.urls import reverse

from stnb.comptes.models import Usuari
from stnb.membres.models import Membre
from stnb.esdeveniments.models import Serie, Esdeveniment


class SerieModelTest(TestCase):
    """Tests for the Serie (Series) model."""

    def test_create_serie(self):
        """Test creating an event series."""
        serie = Serie.objects.create()
        serie.set_current_language('ca')
        serie.nom = 'Number Theory Seminars'
        serie.descripcio = 'Regular seminars on number theory.'
        serie.save()
        self.assertEqual(serie.nom, 'Number Theory Seminars')

    def test_serie_slug_generated_on_save(self):
        """Test that slug is generated from name."""
        serie = Serie.objects.create()
        serie.set_current_language('ca')
        serie.nom = 'Number Theory Seminars'
        serie.descripcio = 'Regular seminars.'
        serie.save()
        self.assertEqual(serie.slug, 'number-theory-seminars')

    def test_serie_str(self):
        """Test string representation."""
        serie = Serie.objects.create()
        serie.set_current_language('ca')
        serie.nom = 'Test Series'
        serie.descripcio = 'A test series.'
        serie.save()
        self.assertEqual(str(serie), 'Test Series')


class EsdevenimentModelTest(TestCase):
    """Tests for the Esdeveniment (Event) model."""

    def setUp(self):
        self.serie = Serie.objects.create()
        self.serie.set_current_language('ca')
        self.serie.nom = 'Test Series'
        self.serie.descripcio = 'A test series.'
        self.serie.save()

    def test_create_esdeveniment(self):
        """Test creating an event."""
        event = Esdeveniment.objects.create(
            serie=self.serie,
            data=datetime.date(2024, 6, 15),
        )
        event.set_current_language('ca')
        event.titol = 'Number Theory Workshop'
        event.abstracte = 'A workshop on number theory.'
        event.lloc = 'Room 101'
        event.save()
        self.assertEqual(event.titol, 'Number Theory Workshop')
        self.assertEqual(event.serie, self.serie)

    def test_esdeveniment_slug_generated_on_save(self):
        """Test slug is generated from title."""
        event = Esdeveniment.objects.create(
            serie=self.serie,
            data=datetime.date(2024, 6, 15),
        )
        event.set_current_language('ca')
        event.titol = 'Number Theory Workshop'
        event.save()
        self.assertEqual(event.slug, 'number-theory-workshop')

    def test_esdeveniment_str(self):
        """Test string representation."""
        event = Esdeveniment.objects.create(
            serie=self.serie,
            data=datetime.date(2024, 6, 15),
        )
        event.set_current_language('ca')
        event.titol = 'Test Event'
        event.save()
        self.assertEqual(str(event), 'Test Event')


class EsdevenimentViewTest(TestCase):
    """Tests for esdeveniment views."""

    def setUp(self):
        self.client = Client()
        self.serie = Serie.objects.create()
        self.serie.set_current_language('ca')
        self.serie.nom = 'Test Series'
        self.serie.descripcio = 'A test series.'
        self.serie.save()

        self.event = Esdeveniment.objects.create(
            serie=self.serie,
            data=datetime.date(2024, 6, 15),
        )
        self.event.set_current_language('ca')
        self.event.titol = 'Test Event'
        self.event.abstracte = 'A test event abstract.'
        self.event.lloc = 'Room 101'
        self.event.save()

    def test_esdeveniment_detail_view(self):
        """Test esdeveniment detail view returns 200."""
        response = self.client.get(
            reverse('esdeveniment-detall', kwargs={'slug': self.event.slug})
        )
        self.assertEqual(response.status_code, 200)
