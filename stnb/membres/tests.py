# -*- coding: utf-8 -*-
"""
Tests for the membres (members) app.
"""
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from stnb.comptes.models import Usuari
from stnb.institucions.models import Institucio
from stnb.membres.models import Membre
from stnb.membres.utils import cognoms_lexic, comparar_cognoms


class MembreModelTest(TestCase):
    """Tests for the Membre (Member) model."""

    def setUp(self):
        self.user = Usuari.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )

    def test_create_membre(self):
        """Test creating a basic member."""
        membre = Membre.objects.language('ca').create(
            user=self.user,
            nom='Joan',
            cognoms='Garcia',
        )
        self.assertEqual(membre.nom, 'Joan')
        self.assertEqual(membre.cognoms, 'Garcia')
        self.assertTrue(membre.membre_actual)
        self.assertFalse(membre.amagar_perfil)

    def test_nom_complet(self):
        """Test nom_complet method with both name and surname."""
        membre = Membre.objects.language('ca').create(
            user=self.user,
            nom='Joan',
            cognoms='Garcia',
        )
        self.assertEqual(membre.nom_complet(), 'Joan Garcia')

    def test_nom_complet_only_nom(self):
        """Test nom_complet with only name."""
        membre = Membre.objects.language('ca').create(
            user=self.user,
            nom='Joan',
        )
        self.assertEqual(membre.nom_complet(), 'Joan')

    def test_nom_complet_only_cognoms(self):
        """Test nom_complet with only surname."""
        membre = Membre.objects.language('ca').create(
            user=self.user,
            cognoms='Garcia',
        )
        self.assertEqual(membre.nom_complet(), 'Garcia')

    def test_nom_complet_none(self):
        """Test nom_complet with neither name nor surname."""
        membre = Membre.objects.language('ca').create(
            user=self.user,
        )
        self.assertIsNone(membre.nom_complet())

    def test_slug_generated_from_name(self):
        """Test that slug is generated from full name."""
        membre = Membre.objects.language('ca').create(
            user=self.user,
            nom='Joan',
            cognoms='Garcia',
        )
        self.assertEqual(membre.slug, 'joan-garcia')

    def test_slug_handles_accents(self):
        """Test that slug handles accented characters."""
        user2 = Usuari.objects.create_user(
            email='test2@example.com',
            password='testpass123'
        )
        membre = Membre.objects.language('ca').create(
            user=user2,
            nom='Josep',
            cognoms='Martinez',
        )
        self.assertIn('josep', membre.slug)
        self.assertIn('martinez', membre.slug)

    def test_unicode_representation(self):
        """Test unicode representation of membre."""
        membre = Membre.objects.language('ca').create(
            user=self.user,
            nom='Joan',
            cognoms='Garcia',
        )
        self.assertEqual(unicode(membre), 'Joan Garcia')

    def test_enllac_a_adds_http(self):
        """Test enllac_a adds http if missing."""
        membre = Membre.objects.language('ca').create(
            user=self.user,
            nom='Joan',
            cognoms='Garcia',
            enllac='www.example.com',
        )
        self.assertEqual(membre.enllac_a(), 'http://www.example.com')

    def test_enllac_a_keeps_https(self):
        """Test enllac_a keeps https if present."""
        membre = Membre.objects.language('ca').create(
            user=self.user,
            nom='Joan',
            cognoms='Garcia',
            enllac='https://www.example.com',
        )
        self.assertEqual(membre.enllac_a(), 'https://www.example.com')

    def test_enllac_a_none(self):
        """Test enllac_a returns None when enllac is None."""
        membre = Membre.objects.language('ca').create(
            user=self.user,
            nom='Joan',
            cognoms='Garcia',
        )
        self.assertIsNone(membre.enllac_a())


class MembreUtilsTest(TestCase):
    """Tests for membre utility functions."""

    def test_cognoms_lexic_dict(self):
        """Test cognoms_lexic with a dictionary."""
        persona = {'nom': 'Joan', 'cognoms': 'Garcia'}
        self.assertEqual(cognoms_lexic(persona), 'garcia')

    def test_cognoms_lexic_removes_de(self):
        """Test cognoms_lexic removes 'de ' prefix."""
        persona = {'nom': 'Joan', 'cognoms': 'de Garcia'}
        self.assertEqual(cognoms_lexic(persona), 'garcia')

    def test_cognoms_lexic_removes_von(self):
        """Test cognoms_lexic removes 'von ' prefix."""
        persona = {'nom': 'Hans', 'cognoms': 'von Schmidt'}
        self.assertEqual(cognoms_lexic(persona), 'schmidt')

    def test_cognoms_lexic_removes_van(self):
        """Test cognoms_lexic removes 'van ' prefix."""
        persona = {'nom': 'Jan', 'cognoms': 'van der Berg'}
        self.assertEqual(cognoms_lexic(persona), 'der berg')

    def test_comparar_cognoms(self):
        """Test comparar_cognoms comparison."""
        persona_a = {'nom': 'Joan', 'cognoms': 'Abril'}
        persona_b = {'nom': 'Pere', 'cognoms': 'Zaragoza'}
        self.assertTrue(comparar_cognoms(persona_a, persona_b))
        self.assertFalse(comparar_cognoms(persona_b, persona_a))


class MembreViewTest(TestCase):
    """Tests for membre views."""

    def setUp(self):
        self.client = Client()
        self.user = Usuari.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
        self.membre = Membre.objects.language('ca').create(
            user=self.user,
            nom='Joan',
            cognoms='Garcia',
            membre_actual=True,
            amagar_perfil=False,
            text='Biography text',
        )

    def test_membre_list_view(self):
        """Test membre list view returns 200."""
        response = self.client.get(reverse('membre-llista'))
        self.assertEqual(response.status_code, 200)

    def test_membre_list_shows_current_members(self):
        """Test that list view shows current members."""
        response = self.client.get(reverse('membre-llista'))
        self.assertContains(response, 'Joan')

    def test_membre_list_hides_hidden_profiles(self):
        """Test that list view hides hidden profiles."""
        user2 = Usuari.objects.create_user(
            email='hidden@example.com',
            password='testpass123'
        )
        Membre.objects.language('ca').create(
            user=user2,
            nom='Hidden',
            cognoms='User',
            amagar_perfil=True,
        )
        response = self.client.get(reverse('membre-llista'))
        self.assertNotContains(response, 'Hidden User')

    def test_membre_detail_view(self):
        """Test membre detail view returns 200."""
        response = self.client.get(
            reverse('membre-detall', kwargs={'slug': self.membre.slug})
        )
        self.assertEqual(response.status_code, 200)

    def test_membre_detail_view_hidden_returns_404(self):
        """Test that hidden membre detail returns 404 for other users."""
        user2 = Usuari.objects.create_user(
            email='hidden@example.com',
            password='testpass123'
        )
        hidden_membre = Membre.objects.language('ca').create(
            user=user2,
            nom='Hidden',
            cognoms='User',
            amagar_perfil=True,
        )
        response = self.client.get(
            reverse('membre-detall', kwargs={'slug': hidden_membre.slug})
        )
        self.assertEqual(response.status_code, 404)

    def test_membre_update_requires_login(self):
        """Test that membre update view requires login."""
        response = self.client.get(
            reverse('membre-actualitzar', kwargs={'slug': self.membre.slug})
        )
        self.assertEqual(response.status_code, 302)

    def test_membre_update_own_profile(self):
        """Test that user can access their own profile update."""
        self.client.login(username='test@example.com', password='testpass123')
        response = self.client.get(
            reverse('membre-actualitzar', kwargs={'slug': self.membre.slug})
        )
        self.assertEqual(response.status_code, 200)

    def test_membre_update_other_profile_forbidden(self):
        """Test that user cannot update another user's profile."""
        user2 = Usuari.objects.create_user(
            email='other@example.com',
            password='testpass123'
        )
        other_membre = Membre.objects.language('ca').create(
            user=user2,
            nom='Other',
            cognoms='User',
        )
        self.client.login(username='test@example.com', password='testpass123')
        response = self.client.get(
            reverse('membre-actualitzar', kwargs={'slug': other_membre.slug})
        )
        self.assertEqual(response.status_code, 403)
