# -*- coding: utf-8 -*-
"""
Tests for the seminaris (seminars) app.
"""
from __future__ import unicode_literals

import datetime

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

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
        seminari = Seminari.objects.language('ca').create(
            slug='test-seminar-2024',
            data_inici=datetime.date(2024, 6, 1),
            data_finalizacio=datetime.date(2024, 6, 5),
            nom='Test Seminar 2024',
            lloc='Barcelona',
            actiu=True,
        )
        self.assertEqual(seminari.slug, 'test-seminar-2024')
        self.assertEqual(seminari.nom, 'Test Seminar 2024')
        self.assertTrue(seminari.actiu)

    def test_seminari_creates_days_on_save(self):
        """Test that saving a seminar creates Dia objects for each day."""
        seminari = Seminari.objects.language('ca').create(
            slug='test-seminar',
            data_inici=datetime.date(2024, 6, 1),
            data_finalizacio=datetime.date(2024, 6, 3),
            nom='Test Seminar',
            lloc='Barcelona',
        )
        self.assertEqual(seminari.dies.count(), 3)

    def test_seminari_unicode(self):
        """Test unicode representation of seminari."""
        seminari = Seminari.objects.language('ca').create(
            slug='test-seminar',
            data_inici=datetime.date(2024, 6, 1),
            data_finalizacio=datetime.date(2024, 6, 3),
            nom='Test Seminar',
            lloc='Barcelona',
        )
        self.assertEqual(unicode(seminari), 'Test Seminar')

    def test_seminari_is_owned_by(self):
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
        seminari = Seminari.objects.language('ca').create(
            slug='test-seminar',
            data_inici=datetime.date(2024, 6, 1),
            data_finalizacio=datetime.date(2024, 6, 3),
            nom='Test Seminar',
            lloc='Barcelona',
        )
        seminari.organitzadors.add(membre)

        self.assertTrue(seminari.is_owned_by(user))

    def test_seminari_not_owned_by_other_user(self):
        """Test is_owned_by returns False for non-organizer."""
        user = Usuari.objects.create_user(
            email='other@example.com',
            password='testpass123'
        )
        Membre.objects.language('ca').create(
            user=user,
            nom='Other',
            cognoms='User',
        )
        seminari = Seminari.objects.language('ca').create(
            slug='test-seminar',
            data_inici=datetime.date(2024, 6, 1),
            data_finalizacio=datetime.date(2024, 6, 3),
            nom='Test Seminar',
            lloc='Barcelona',
        )
        self.assertFalse(seminari.is_owned_by(user))

    def test_calendari_definit_empty(self):
        """Test calendari_definit returns False when no items."""
        seminari = Seminari.objects.language('ca').create(
            slug='test-seminar',
            data_inici=datetime.date(2024, 6, 1),
            data_finalizacio=datetime.date(2024, 6, 1),
            nom='Test Seminar',
            lloc='Barcelona',
        )
        self.assertFalse(seminari.calendari_definit())


class TemaModelTest(TestCase):
    """Tests for the Tema (Theme) model."""

    def setUp(self):
        self.seminari = Seminari.objects.language('ca').create(
            slug='test-seminar',
            data_inici=datetime.date(2024, 6, 1),
            data_finalizacio=datetime.date(2024, 6, 3),
            nom='Test Seminar',
            lloc='Barcelona',
        )

    def test_create_tema(self):
        """Test creating a theme."""
        tema = Tema.objects.language('ca').create(
            seminari=self.seminari,
            ordre=1,
            titol='Algebraic Number Theory',
            descripcio='Introduction to algebraic number theory.',
        )
        self.assertEqual(tema.titol, 'Algebraic Number Theory')
        self.assertEqual(tema.seminari, self.seminari)

    def test_tema_unicode(self):
        """Test unicode representation includes seminar name."""
        tema = Tema.objects.language('ca').create(
            seminari=self.seminari,
            ordre=1,
            titol='Algebraic Number Theory',
        )
        self.assertIn('Algebraic Number Theory', unicode(tema))
        self.assertIn('Test Seminar', unicode(tema))


class XerradaModelTest(TestCase):
    """Tests for the Xerrada (Talk) model."""

    def setUp(self):
        self.seminari = Seminari.objects.language('ca').create(
            slug='test-seminar',
            data_inici=datetime.date(2024, 6, 1),
            data_finalizacio=datetime.date(2024, 6, 3),
            nom='Test Seminar',
            lloc='Barcelona',
        )
        self.tema = Tema.objects.language('ca').create(
            seminari=self.seminari,
            ordre=1,
            titol='Algebraic Number Theory',
        )

    def test_create_xerrada(self):
        """Test creating a talk."""
        xerrada = Xerrada.objects.language('ca').create(
            tema=self.tema,
            ordre=1,
            titol='Introduction to p-adic Numbers',
            abstracte='An overview of p-adic number theory.',
        )
        self.assertEqual(xerrada.titol, 'Introduction to p-adic Numbers')
        self.assertEqual(xerrada.tema, self.tema)

    def test_xerrada_seminari_via_tema(self):
        """Test xerrada.seminari() returns the correct seminar."""
        xerrada = Xerrada.objects.language('ca').create(
            tema=self.tema,
            ordre=1,
            titol='Test Talk',
        )
        self.assertEqual(xerrada.seminari(), self.seminari)

    def test_xerrada_is_owned_by_presenter(self):
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
        xerrada = Xerrada.objects.language('ca').create(
            tema=self.tema,
            ordre=1,
            titol='Test Talk',
        )
        xerrada.presentadors.add(membre)

        self.assertTrue(xerrada.is_owned_by(user))


class ItemProgramaModelTest(TestCase):
    """Tests for the ItemPrograma (Programme Item) model."""

    def setUp(self):
        self.seminari = Seminari.objects.language('ca').create(
            slug='test-seminar',
            data_inici=datetime.date(2024, 6, 1),
            data_finalizacio=datetime.date(2024, 6, 1),
            nom='Test Seminar',
            lloc='Barcelona',
        )
        self.dia = self.seminari.dies.first()
        self.tema = Tema.objects.language('ca').create(
            seminari=self.seminari,
            ordre=1,
            titol='Test Theme',
        )
        self.xerrada = Xerrada.objects.language('ca').create(
            tema=self.tema,
            ordre=1,
            titol='Test Talk',
        )

    def test_create_item_programa(self):
        """Test creating a programme item."""
        item = ItemPrograma.objects.language('ca').create(
            xerrada=self.xerrada,
            dia=self.dia,
            hora_inici=datetime.time(9, 0),
            hora_finalizacio=datetime.time(10, 0),
        )
        self.assertEqual(item.xerrada, self.xerrada)
        self.assertEqual(item.dia, self.dia)

    def test_item_programa_duracio(self):
        """Test duracio method."""
        item = ItemPrograma.objects.language('ca').create(
            xerrada=self.xerrada,
            dia=self.dia,
            hora_inici=datetime.time(9, 0),
            hora_finalizacio=datetime.time(10, 30),
        )
        self.assertEqual(item.duracio(), '09.00 - 10.30')

    def test_item_programa_titol_from_xerrada(self):
        """Test titol returns xerrada title."""
        item = ItemPrograma.objects.language('ca').create(
            xerrada=self.xerrada,
            dia=self.dia,
            hora_inici=datetime.time(9, 0),
            hora_finalizacio=datetime.time(10, 0),
        )
        self.assertEqual(item.titol(), 'Test Talk')

    def test_item_programa_titol_from_descripcio(self):
        """Test titol returns descripcio when no xerrada."""
        item = ItemPrograma.objects.language('ca').create(
            dia=self.dia,
            hora_inici=datetime.time(12, 0),
            hora_finalizacio=datetime.time(13, 0),
            descripcio='Lunch Break',
        )
        self.assertEqual(item.titol(), 'Lunch Break')


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
        self.seminari = Seminari.objects.language('ca').create(
            slug='test-seminar-2024',
            data_inici=datetime.date(2024, 6, 1),
            data_finalizacio=datetime.date(2024, 6, 3),
            nom='Test Seminar 2024',
            lloc='Barcelona',
            actiu=True,
        )

    def test_seminari_list_view(self):
        """Test seminari list view returns 200."""
        response = self.client.get(reverse('seminari-llista'))
        self.assertEqual(response.status_code, 200)

    def test_seminari_list_shows_active_seminars(self):
        """Test that list view shows active seminars."""
        response = self.client.get(reverse('seminari-llista'))
        self.assertContains(response, 'Test Seminar 2024')

    def test_seminari_list_hides_inactive_seminars(self):
        """Test that list view hides inactive seminars."""
        Seminari.objects.language('ca').create(
            slug='inactive-seminar',
            data_inici=datetime.date(2024, 1, 1),
            data_finalizacio=datetime.date(2024, 1, 3),
            nom='Inactive Seminar',
            lloc='Barcelona',
            actiu=False,
        )
        response = self.client.get(reverse('seminari-llista'))
        self.assertNotContains(response, 'Inactive Seminar')

    def test_seminari_detail_view(self):
        """Test seminari detail view returns 200."""
        response = self.client.get(
            reverse('seminari-detall', kwargs={'slug': self.seminari.slug})
        )
        self.assertEqual(response.status_code, 200)

    def test_seminari_detail_view_inactive_returns_404(self):
        """Test that inactive seminar detail returns 404."""
        inactive = Seminari.objects.language('ca').create(
            slug='inactive-seminar',
            data_inici=datetime.date(2024, 1, 1),
            data_finalizacio=datetime.date(2024, 1, 3),
            nom='Inactive Seminar',
            lloc='Barcelona',
            actiu=False,
        )
        response = self.client.get(
            reverse('seminari-detall', kwargs={'slug': inactive.slug})
        )
        self.assertEqual(response.status_code, 404)

    def test_seminari_actual_redirects(self):
        """Test seminari actual view redirects to active seminar."""
        response = self.client.get(reverse('seminari-actual'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(self.seminari.slug, response.url)

    def test_seminari_actual_no_active_returns_404(self):
        """Test seminari actual returns 404 when no active seminars."""
        self.seminari.actiu = False
        self.seminari.save()
        response = self.client.get(reverse('seminari-actual'))
        self.assertEqual(response.status_code, 404)


class TemaViewTest(TestCase):
    """Tests for tema views."""

    def setUp(self):
        self.client = Client()
        self.seminari = Seminari.objects.language('ca').create(
            slug='test-seminar',
            data_inici=datetime.date(2024, 6, 1),
            data_finalizacio=datetime.date(2024, 6, 3),
            nom='Test Seminar',
            lloc='Barcelona',
            actiu=True,
        )
        self.tema = Tema.objects.language('ca').create(
            seminari=self.seminari,
            ordre=1,
            titol='Test Theme',
            descripcio='A test theme.',
        )

    def test_tema_detail_view(self):
        """Test tema detail view returns 200."""
        response = self.client.get(
            reverse('seminari-tema-detall', kwargs={
                'seminari_slug': self.seminari.slug,
                'tema_id': self.tema.pk,
            })
        )
        self.assertEqual(response.status_code, 200)

    def test_tema_detail_wrong_seminar_returns_404(self):
        """Test tema detail with wrong seminar returns 404."""
        other_seminari = Seminari.objects.language('ca').create(
            slug='other-seminar',
            data_inici=datetime.date(2024, 7, 1),
            data_finalizacio=datetime.date(2024, 7, 3),
            nom='Other Seminar',
            lloc='Madrid',
            actiu=True,
        )
        response = self.client.get(
            reverse('seminari-tema-detall', kwargs={
                'seminari_slug': other_seminari.slug,
                'tema_id': self.tema.pk,
            })
        )
        self.assertEqual(response.status_code, 404)


class XerradaViewTest(TestCase):
    """Tests for xerrada views."""

    def setUp(self):
        self.client = Client()
        self.user = Usuari.objects.create_user(
            email='presenter@example.com',
            password='testpass123'
        )
        self.membre = Membre.objects.language('ca').create(
            user=self.user,
            nom='Test',
            cognoms='Presenter',
        )
        self.seminari = Seminari.objects.language('ca').create(
            slug='test-seminar',
            data_inici=datetime.date(2024, 6, 1),
            data_finalizacio=datetime.date(2024, 6, 3),
            nom='Test Seminar',
            lloc='Barcelona',
            actiu=True,
        )
        self.tema = Tema.objects.language('ca').create(
            seminari=self.seminari,
            ordre=1,
            titol='Test Theme',
        )
        self.xerrada = Xerrada.objects.language('ca').create(
            tema=self.tema,
            ordre=1,
            titol='Test Talk',
            abstracte='A test talk abstract.',
        )
        self.xerrada.presentadors.add(self.membre)

    def test_xerrada_detail_view(self):
        """Test xerrada detail view returns 200."""
        response = self.client.get(
            reverse('seminari-xerrada-detall', kwargs={
                'seminari_slug': self.seminari.slug,
                'xerrada_id': self.xerrada.pk,
            })
        )
        self.assertEqual(response.status_code, 200)

    def test_xerrada_update_requires_login(self):
        """Test xerrada update requires login."""
        response = self.client.get(
            reverse('seminari-xerrada-actualitzar', kwargs={
                'seminari_slug': self.seminari.slug,
                'xerrada_id': self.xerrada.pk,
            })
        )
        self.assertEqual(response.status_code, 302)

    def test_xerrada_update_by_presenter(self):
        """Test presenter can access xerrada update."""
        self.client.login(username='presenter@example.com', password='testpass123')
        response = self.client.get(
            reverse('seminari-xerrada-actualitzar', kwargs={
                'seminari_slug': self.seminari.slug,
                'xerrada_id': self.xerrada.pk,
            })
        )
        self.assertEqual(response.status_code, 200)

    def test_xerrada_update_forbidden_for_others(self):
        """Test non-presenter cannot access xerrada update."""
        other_user = Usuari.objects.create_user(
            email='other@example.com',
            password='testpass123'
        )
        Membre.objects.language('ca').create(
            user=other_user,
            nom='Other',
            cognoms='User',
        )
        self.client.login(username='other@example.com', password='testpass123')
        response = self.client.get(
            reverse('seminari-xerrada-actualitzar', kwargs={
                'seminari_slug': self.seminari.slug,
                'xerrada_id': self.xerrada.pk,
            })
        )
        self.assertEqual(response.status_code, 403)
