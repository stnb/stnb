# -*- coding: utf-8 -*-
"""
Tests for the esdeveniments (events) app.
"""
from __future__ import unicode_literals

import datetime

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from stnb.comptes.models import Usuari
from stnb.membres.models import Membre
from stnb.esdeveniments.models import Serie, Esdeveniment


class SerieModelTest(TestCase):
    """Tests for the Serie (Series) model."""

    def test_create_serie(self):
        """Test creating an event series."""
        serie = Serie.objects.language('ca').create(
            nom='Number Theory Seminars',
            descripcio='Regular seminars on number theory.',
        )
        self.assertEqual(serie.nom, 'Number Theory Seminars')

    def test_serie_slug_generated_on_save(self):
        """Test that slug is generated from name."""
        serie = Serie.objects.language('ca').create(
            nom='Number Theory Seminars',
            descripcio='Regular seminars.',
        )
        self.assertEqual(serie.slug, 'number-theory-seminars')

    def test_serie_unicode(self):
        """Test unicode representation."""
        serie = Serie.objects.language('ca').create(
            nom='Test Series',
            descripcio='A test series.',
        )
        self.assertEqual(unicode(serie), 'Test Series')

    def test_serie_is_owned_by(self):
        """Test is_owned_by method."""
        user = Usuari.objects.create_user(
            email='organizer@example.com',
            password='testpass123'
        )
        membre = Membre.objects.language('ca').create(
            user=user,
            nom='Test',
            cognoms='Organizer',
        )
        serie = Serie.objects.language('ca').create(
            nom='Test Series',
            descripcio='A test series.',
        )
        serie.organitzadors.add(membre)
        self.assertTrue(serie.is_owned_by(user))

    def test_nombre_de_esdeveniments(self):
        """Test nombre_de_esdeveniments counts events."""
        serie = Serie.objects.language('ca').create(
            nom='Test Series',
            descripcio='A test series.',
        )
        self.assertEqual(serie.nombre_de_esdeveniments(), 0)

        Esdeveniment.objects.language('ca').create(
            serie=serie,
            data=datetime.date(2024, 6, 1),
            titol='Event 1',
        )
        self.assertEqual(serie.nombre_de_esdeveniments(), 1)


class EsdevenimentModelTest(TestCase):
    """Tests for the Esdeveniment (Event) model."""

    def setUp(self):
        self.serie = Serie.objects.language('ca').create(
            nom='Test Series',
            descripcio='A test series.',
        )

    def test_create_esdeveniment(self):
        """Test creating an event."""
        event = Esdeveniment.objects.language('ca').create(
            serie=self.serie,
            data=datetime.date(2024, 6, 15),
            titol='Number Theory Workshop',
            abstracte='A workshop on number theory.',
            lloc='Room 101',
        )
        self.assertEqual(event.titol, 'Number Theory Workshop')
        self.assertEqual(event.serie, self.serie)

    def test_esdeveniment_slug_generated_on_save(self):
        """Test slug is generated from title."""
        event = Esdeveniment.objects.language('ca').create(
            serie=self.serie,
            data=datetime.date(2024, 6, 15),
            titol='Number Theory Workshop',
        )
        self.assertEqual(event.slug, 'number-theory-workshop')

    def test_esdeveniment_unicode(self):
        """Test unicode representation."""
        event = Esdeveniment.objects.language('ca').create(
            serie=self.serie,
            data=datetime.date(2024, 6, 15),
            titol='Test Event',
        )
        self.assertEqual(unicode(event), 'Test Event')

    def test_esdeveniment_with_times(self):
        """Test event with start and end times."""
        event = Esdeveniment.objects.language('ca').create(
            serie=self.serie,
            data=datetime.date(2024, 6, 15),
            hora_inici=datetime.time(10, 0),
            hora_finalizacio=datetime.time(12, 0),
            titol='Morning Workshop',
        )
        self.assertEqual(event.hora_inici, datetime.time(10, 0))
        self.assertEqual(event.hora_finalizacio, datetime.time(12, 0))

    def test_esdeveniment_is_owned_by_host(self):
        """Test is_owned_by for host."""
        user = Usuari.objects.create_user(
            email='host@example.com',
            password='testpass123'
        )
        membre = Membre.objects.language('ca').create(
            user=user,
            nom='Test',
            cognoms='Host',
        )
        event = Esdeveniment.objects.language('ca').create(
            serie=self.serie,
            data=datetime.date(2024, 6, 15),
            titol='Test Event',
        )
        event.amfitrions.add(membre)
        self.assertTrue(event.is_owned_by(user))

    def test_esdeveniment_is_owned_by_presenter(self):
        """Test is_owned_by for presenter."""
        user = Usuari.objects.create_user(
            email='presenter@example.com',
            password='testpass123'
        )
        membre = Membre.objects.language('ca').create(
            user=user,
            nom='Test',
            cognoms='Presenter',
        )
        event = Esdeveniment.objects.language('ca').create(
            serie=self.serie,
            data=datetime.date(2024, 6, 15),
            titol='Test Event',
        )
        event.presentadors.add(membre)
        self.assertTrue(event.is_owned_by(user))

    def test_esdeveniment_is_owned_by_series_organizer(self):
        """Test is_owned_by for series organizer."""
        user = Usuari.objects.create_user(
            email='organizer@example.com',
            password='testpass123'
        )
        membre = Membre.objects.language('ca').create(
            user=user,
            nom='Test',
            cognoms='Organizer',
        )
        self.serie.organitzadors.add(membre)

        event = Esdeveniment.objects.language('ca').create(
            serie=self.serie,
            data=datetime.date(2024, 6, 15),
            titol='Test Event',
        )
        self.assertTrue(event.is_owned_by(user))

    def test_esdeveniment_without_serie(self):
        """Test event without a series."""
        event = Esdeveniment.objects.language('ca').create(
            data=datetime.date(2024, 6, 15),
            titol='Standalone Event',
        )
        self.assertIsNone(event.serie)


class EsdevenimentViewTest(TestCase):
    """Tests for esdeveniment views."""

    def setUp(self):
        self.client = Client()
        self.serie = Serie.objects.language('ca').create(
            nom='Test Series',
            descripcio='A test series.',
        )
        self.event = Esdeveniment.objects.language('ca').create(
            serie=self.serie,
            data=datetime.date(2024, 6, 15),
            titol='Test Event',
            abstracte='A test event abstract.',
            lloc='Room 101',
        )

    def test_esdeveniment_detail_view(self):
        """Test esdeveniment detail view returns 200."""
        response = self.client.get(
            reverse('esdeveniment-detall', kwargs={'slug': self.event.slug})
        )
        self.assertEqual(response.status_code, 200)

    def test_esdeveniment_detail_contains_title(self):
        """Test detail view contains event title."""
        response = self.client.get(
            reverse('esdeveniment-detall', kwargs={'slug': self.event.slug})
        )
        self.assertContains(response, 'Test Event')

    def test_esdeveniment_update_requires_login(self):
        """Test event file update requires login."""
        response = self.client.get(
            reverse('esdeveniment-fitxer-actualitzar', kwargs={'slug': self.event.slug})
        )
        self.assertEqual(response.status_code, 302)

    def test_esdeveniment_update_by_presenter(self):
        """Test presenter can update event files."""
        user = Usuari.objects.create_user(
            email='presenter@example.com',
            password='testpass123'
        )
        membre = Membre.objects.language('ca').create(
            user=user,
            nom='Test',
            cognoms='Presenter',
        )
        self.event.presentadors.add(membre)

        self.client.login(username='presenter@example.com', password='testpass123')
        response = self.client.get(
            reverse('esdeveniment-fitxer-actualitzar', kwargs={'slug': self.event.slug})
        )
        self.assertEqual(response.status_code, 200)

    def test_esdeveniment_update_forbidden_for_others(self):
        """Test non-owner cannot update event files."""
        user = Usuari.objects.create_user(
            email='other@example.com',
            password='testpass123'
        )
        Membre.objects.language('ca').create(
            user=user,
            nom='Other',
            cognoms='User',
        )

        self.client.login(username='other@example.com', password='testpass123')
        response = self.client.get(
            reverse('esdeveniment-fitxer-actualitzar', kwargs={'slug': self.event.slug})
        )
        self.assertEqual(response.status_code, 403)
