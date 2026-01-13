# -*- coding: utf-8 -*-
"""
Tests for the i18n (internationalization) app.
"""
from django.test import TestCase, Client
from django.urls import reverse


class SetLanguageViewTest(TestCase):
    """Tests for the set_language view."""

    def setUp(self):
        self.client = Client()

    def test_set_language_get_redirect(self):
        """Test that set-language redirects on GET."""
        response = self.client.get(
            reverse('set-language') + '?language=ca',
            HTTP_REFERER='/'
        )
        self.assertEqual(response.status_code, 302)

    def test_set_language_redirect_to_referer(self):
        """Test that set-language redirects to referer."""
        response = self.client.get(
            reverse('set-language') + '?language=es',
            HTTP_REFERER='/ca/membres/'
        )
        self.assertEqual(response.status_code, 302)
