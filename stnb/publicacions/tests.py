# -*- coding: utf-8 -*-
"""
Tests for the publicacions (publications) app.
"""
from __future__ import unicode_literals

import datetime

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from stnb.comptes.models import Usuari
from stnb.membres.models import Membre
from stnb.publicacions.models import Publicacio


class PublicacioModelTest(TestCase):
    """Tests for the Publicacio (Publication) model."""

    def test_create_publicacio(self):
        """Test creating a publication."""
        pub = Publicacio.objects.language('ca').create(
            nom='Introduction to Number Theory',
            descripcio='A comprehensive guide.',
            isbn='978-0-12-345678-9',
            data_publicacio=datetime.date(2024, 3, 15),
        )
        self.assertEqual(pub.nom, 'Introduction to Number Theory')
        self.assertEqual(pub.isbn, '978-0-12-345678-9')

    def test_publicacio_unicode(self):
        """Test unicode representation."""
        pub = Publicacio.objects.language('ca').create(
            nom='Test Publication',
            descripcio='A test.',
        )
        self.assertEqual(unicode(pub), 'Test Publication')

    def test_publicacio_with_autors(self):
        """Test publication with authors."""
        user = Usuari.objects.create_user(
            email='author@example.com',
            password='testpass123'
        )
        membre = Membre.objects.language('ca').create(
            user=user,
            nom='Test',
            cognoms='Author',
        )
        pub = Publicacio.objects.language('ca').create(
            nom='Test Publication',
            descripcio='A test.',
        )
        pub.autors.add(membre)
        self.assertIn(membre, pub.autors.all())

    def test_publicacio_with_editors(self):
        """Test publication with editors."""
        user = Usuari.objects.create_user(
            email='editor@example.com',
            password='testpass123'
        )
        membre = Membre.objects.language('ca').create(
            user=user,
            nom='Test',
            cognoms='Editor',
        )
        pub = Publicacio.objects.language('ca').create(
            nom='Test Publication',
            descripcio='A test.',
        )
        pub.editors.add(membre)
        self.assertIn(membre, pub.editors.all())

    def test_mes_any_publicacio(self):
        """Test mes_any_publicacio method."""
        pub = Publicacio.objects.language('ca').create(
            nom='Test Publication',
            descripcio='A test.',
            data_publicacio=datetime.date(2024, 6, 15),
        )
        result = pub.mes_any_publicacio()
        self.assertIn('2024', result)

    def test_publicacio_with_translation(self):
        """Test publication with translations."""
        pub = Publicacio.objects.language('ca').create(
            nom='Teoria de Nombres',
            descripcio='Sobre nombres.',
        )
        pub.translate('es')
        pub.nom = 'Teoria de Numeros'
        pub.descripcio = 'Sobre numeros.'
        pub.save()

        pub_ca = Publicacio.objects.language('ca').get(pk=pub.pk)
        self.assertEqual(pub_ca.nom, 'Teoria de Nombres')

        pub_es = Publicacio.objects.language('es').get(pk=pub.pk)
        self.assertEqual(pub_es.nom, 'Teoria de Numeros')

    def test_publicacio_altres_autors(self):
        """Test publication with other (non-member) authors."""
        pub = Publicacio.objects.language('ca').create(
            nom='Test Publication',
            descripcio='A test.',
            altres_autors='John Smith, Jane Doe',
        )
        self.assertEqual(pub.altres_autors, 'John Smith, Jane Doe')


class PublicacioViewTest(TestCase):
    """Tests for publicacio views."""

    def setUp(self):
        self.client = Client()
        self.publicacio = Publicacio.objects.language('ca').create(
            nom='Test Publication',
            descripcio='A test publication.',
            data_publicacio=datetime.date(2024, 3, 15),
        )

    def test_publicacio_list_view(self):
        """Test publicacio list view returns 200."""
        response = self.client.get(reverse('publicacio-llista'))
        self.assertEqual(response.status_code, 200)

    def test_publicacio_list_contains_publication(self):
        """Test list view contains publication."""
        response = self.client.get(reverse('publicacio-llista'))
        self.assertContains(response, 'Test Publication')
