# -*- coding: utf-8 -*-
"""
Tests for the noticies (news) app.
"""
from __future__ import unicode_literals

import datetime

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.utils import timezone

from stnb.noticies.models import Noticia, MicroAlerta


class NoticiaModelTest(TestCase):
    """Tests for the Noticia (News) model."""

    def test_create_noticia(self):
        """Test creating a news item."""
        noticia = Noticia.objects.language('ca').create(
            data=timezone.now(),
            titol='Important Announcement',
            descripcio='This is an important announcement.',
        )
        self.assertEqual(noticia.titol, 'Important Announcement')

    def test_noticia_unicode(self):
        """Test unicode representation."""
        noticia = Noticia.objects.language('ca').create(
            data=timezone.now(),
            titol='Test News',
            descripcio='Test description.',
        )
        self.assertEqual(unicode(noticia), 'Test News')

    def test_noticia_creat_auto(self):
        """Test that creat is set automatically."""
        before = timezone.now()
        noticia = Noticia.objects.language('ca').create(
            data=timezone.now(),
            titol='Test News',
            descripcio='Test description.',
        )
        after = timezone.now()
        self.assertGreaterEqual(noticia.creat, before)
        self.assertLessEqual(noticia.creat, after)

    def test_noticia_actualizat_auto(self):
        """Test that actualizat is updated on save."""
        noticia = Noticia.objects.language('ca').create(
            data=timezone.now(),
            titol='Test News',
            descripcio='Test description.',
        )
        original_update = noticia.actualizat

        noticia.titol = 'Updated News'
        noticia.save()

        noticia = Noticia.objects.language('ca').get(pk=noticia.pk)
        self.assertGreaterEqual(noticia.actualizat, original_update)

    def test_noticia_ordering(self):
        """Test that news items are ordered by date descending."""
        old_news = Noticia.objects.language('ca').create(
            data=timezone.now() - datetime.timedelta(days=7),
            titol='Old News',
            descripcio='Old description.',
        )
        new_news = Noticia.objects.language('ca').create(
            data=timezone.now(),
            titol='New News',
            descripcio='New description.',
        )
        noticies = list(Noticia.objects.all())
        self.assertEqual(noticies[0].pk, new_news.pk)
        self.assertEqual(noticies[1].pk, old_news.pk)

    def test_noticia_with_translation(self):
        """Test news item with translations."""
        noticia = Noticia.objects.language('ca').create(
            data=timezone.now(),
            titol='Titol Catala',
            descripcio='Descripcio catalana.',
        )
        noticia.translate('es')
        noticia.titol = 'Titulo Espanol'
        noticia.descripcio = 'Descripcion espanola.'
        noticia.save()

        noticia_ca = Noticia.objects.language('ca').get(pk=noticia.pk)
        self.assertEqual(noticia_ca.titol, 'Titol Catala')

        noticia_es = Noticia.objects.language('es').get(pk=noticia.pk)
        self.assertEqual(noticia_es.titol, 'Titulo Espanol')


class MicroAlertaModelTest(TestCase):
    """Tests for the MicroAlerta model."""

    def test_create_microalerta(self):
        """Test creating a microalert."""
        alerta = MicroAlerta.objects.language('ca').create(
            data=timezone.now(),
            alerta='Registration is now open!',
        )
        self.assertEqual(alerta.alerta, 'Registration is now open!')

    def test_microalerta_unicode(self):
        """Test unicode representation."""
        alerta = MicroAlerta.objects.language('ca').create(
            data=timezone.now(),
            alerta='Test Alert',
        )
        self.assertEqual(unicode(alerta), 'Test Alert')

    def test_microalerta_ordering(self):
        """Test that alerts are ordered by date descending."""
        old_alert = MicroAlerta.objects.language('ca').create(
            data=timezone.now() - datetime.timedelta(days=7),
            alerta='Old Alert',
        )
        new_alert = MicroAlerta.objects.language('ca').create(
            data=timezone.now(),
            alerta='New Alert',
        )
        alertes = list(MicroAlerta.objects.all())
        self.assertEqual(alertes[0].pk, new_alert.pk)
        self.assertEqual(alertes[1].pk, old_alert.pk)


class NoticiesViewTest(TestCase):
    """Tests for noticies views."""

    def setUp(self):
        self.client = Client()
        self.noticia = Noticia.objects.language('ca').create(
            data=timezone.now(),
            titol='Test News Item',
            descripcio='This is a test news item.',
        )

    def test_inici_view(self):
        """Test home page view returns 200."""
        response = self.client.get(reverse('inici'))
        self.assertEqual(response.status_code, 200)

    def test_inici_view_contains_news(self):
        """Test home page contains news."""
        response = self.client.get(reverse('inici'))
        self.assertContains(response, 'Test News Item')

    def test_noticies_ultimes_view(self):
        """Test recent news view returns 200."""
        response = self.client.get(reverse('noticies-ultimes'))
        self.assertEqual(response.status_code, 200)
