# -*- coding: utf-8 -*-
"""
Tests for the publicacions (publications) app.
"""
import datetime

from django.test import TestCase, Client
from django.urls import reverse

from stnb.comptes.models import Usuari
from stnb.membres.models import Membre
from stnb.publicacions.models import Publicacio


class PublicacioModelTest(TestCase):
    """Tests for the Publicacio (Publication) model."""

    def test_create_publicacio(self):
        """Test creating a publication."""
        pub = Publicacio.objects.create(
            isbn='978-0-12-345678-9',
            data_publicacio=datetime.date(2024, 3, 15),
        )
        pub.set_current_language('ca')
        pub.nom = 'Introduction to Number Theory'
        pub.descripcio = 'A comprehensive guide.'
        pub.save()
        self.assertEqual(pub.nom, 'Introduction to Number Theory')
        self.assertEqual(pub.isbn, '978-0-12-345678-9')

    def test_publicacio_str(self):
        """Test string representation."""
        pub = Publicacio.objects.create()
        pub.set_current_language('ca')
        pub.nom = 'Test Publication'
        pub.descripcio = 'A test.'
        pub.save()
        self.assertEqual(str(pub), 'Test Publication')

    def test_publicacio_with_autors(self):
        """Test publication with authors."""
        user = Usuari.objects.create_user(
            email='author@example.com',
            password='testpass123'
        )
        membre = Membre.objects.create(
            user=user,
            nom='Test',
            cognoms='Author',
        )
        pub = Publicacio.objects.create()
        pub.set_current_language('ca')
        pub.nom = 'Test Publication'
        pub.descripcio = 'A test.'
        pub.save()
        pub.autors.add(membre)
        self.assertIn(membre, pub.autors.all())

    def test_publicacio_altres_autors(self):
        """Test publication with other (non-member) authors."""
        pub = Publicacio.objects.create(
            altres_autors='John Smith, Jane Doe',
        )
        pub.set_current_language('ca')
        pub.nom = 'Test Publication'
        pub.descripcio = 'A test.'
        pub.save()
        self.assertEqual(pub.altres_autors, 'John Smith, Jane Doe')


class PublicacioViewTest(TestCase):
    """Tests for publicacio views."""

    def setUp(self):
        self.client = Client()
        self.publicacio = Publicacio.objects.create(
            data_publicacio=datetime.date(2024, 3, 15),
        )
        self.publicacio.set_current_language('ca')
        self.publicacio.nom = 'Test Publication'
        self.publicacio.descripcio = 'A test publication.'
        self.publicacio.save()

    def test_publicacio_list_view(self):
        """Test publicacio list view returns 200."""
        response = self.client.get(reverse('publicacio-llista'))
        self.assertEqual(response.status_code, 200)
