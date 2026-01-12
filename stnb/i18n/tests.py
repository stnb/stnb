# -*- coding: utf-8 -*-
"""
Tests for the i18n (internationalization) app.
"""
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class SetLanguageViewTest(TestCase):
    """Tests for the set_language view."""

    def setUp(self):
        self.client = Client()

    def test_set_language_to_catalan(self):
        """Test setting language to Catalan."""
        response = self.client.post(
            reverse('set-language'),
            {'language': 'ca'},
            HTTP_REFERER='/'
        )
        self.assertEqual(response.status_code, 302)

    def test_set_language_to_spanish(self):
        """Test setting language to Spanish."""
        response = self.client.post(
            reverse('set-language'),
            {'language': 'es'},
            HTTP_REFERER='/'
        )
        self.assertEqual(response.status_code, 302)

    def test_set_language_to_english(self):
        """Test setting language to English."""
        response = self.client.post(
            reverse('set-language'),
            {'language': 'en'},
            HTTP_REFERER='/'
        )
        self.assertEqual(response.status_code, 302)
