# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models, connection


def migrate_users(apps, schema_editor):
    """Migrate users from auth_user to comptes_usuari if auth_user exists."""
    cursor = connection.cursor()
    # Check if auth_user table exists
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='auth_user'"
        if connection.vendor == 'sqlite' else
        "SELECT table_name FROM information_schema.tables WHERE table_name='auth_user'"
    )
    if cursor.fetchone():
        # auth_user exists, migrate the data
        cursor.execute('''
            INSERT INTO comptes_usuari
                ( id, password, last_login, is_superuser, email,
                  nom, cognoms,
                  is_staff, is_active, date_joined )
                SELECT a.id, a.password, a.last_login, a.is_superuser, a.email,
                       a.first_name, a.last_name, a.is_staff, a.is_active, a.date_joined
                FROM auth_user `a`
        ''')
        cursor.execute('''
            INSERT INTO comptes_usuari_groups ( id, usuari_id, group_id )
                SELECT a.id, a.user_id, a.group_id FROM auth_user_groups `a`
        ''')


class Migration(migrations.Migration):

    dependencies = [
        ('publicacions', '0002_auto_20150611_1554'),
    ]

    operations = [
        migrations.RunPython(migrate_users, migrations.RunPython.noop),
    ]
