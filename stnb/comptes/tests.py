# -*- coding: utf-8 -*-
"""
Tests for the comptes (accounts) app.
"""
from django.test import TestCase
from django.utils import timezone

from stnb.comptes.models import Usuari
from stnb.comptes.managers import UsuariGerent


class UsuariModelTest(TestCase):
    """Tests for the Usuari (User) model."""

    def test_create_user(self):
        """Test creating a basic user."""
        user = Usuari.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpass123'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_without_email_raises_error(self):
        """Test that creating a user without email raises ValueError."""
        with self.assertRaises(ValueError):
            Usuari.objects.create_user(email='', password='testpass123')

    def test_email_is_normalized(self):
        """Test that email addresses are normalized."""
        user = Usuari.objects.create_user(
            email='Test@EXAMPLE.com',
            password='testpass123'
        )
        self.assertEqual(user.email, 'Test@example.com')

    def test_username_property_returns_email(self):
        """Test that username property returns email."""
        user = Usuari.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'test@example.com')

    def test_get_full_name_returns_email(self):
        """Test get_full_name returns email."""
        user = Usuari.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
        self.assertEqual(user.get_full_name(), 'test@example.com')

    def test_get_short_name_returns_email(self):
        """Test get_short_name returns email."""
        user = Usuari.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
        self.assertEqual(user.get_short_name(), 'test@example.com')

    def test_user_date_joined_set_automatically(self):
        """Test that date_joined is set automatically."""
        before = timezone.now()
        user = Usuari.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
        after = timezone.now()
        self.assertGreaterEqual(user.date_joined, before)
        self.assertLessEqual(user.date_joined, after)

    def test_user_with_nom_and_cognoms(self):
        """Test creating user with name and surname."""
        user = Usuari.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
        user.nom = 'Joan'
        user.cognoms = 'Garcia'
        user.save()

        user = Usuari.objects.get(email='test@example.com')
        self.assertEqual(user.nom, 'Joan')
        self.assertEqual(user.cognoms, 'Garcia')


class UsuariGerentTest(TestCase):
    """Tests for the UsuariGerent (User Manager) class."""

    def test_get_by_natural_key_case_insensitive(self):
        """Test that get_by_natural_key is case insensitive."""
        Usuari.objects.create_user(
            email='Test@Example.com',
            password='testpass123'
        )
        user = Usuari.objects.get_by_natural_key('test@example.com')
        self.assertEqual(user.email, 'Test@example.com')

    def test_create_user_sets_is_active_true(self):
        """Test that create_user sets is_active to True."""
        user = Usuari.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
        self.assertTrue(user.is_active)

    def test_create_user_sets_is_staff_false(self):
        """Test that create_user sets is_staff to False."""
        user = Usuari.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
        self.assertFalse(user.is_staff)
