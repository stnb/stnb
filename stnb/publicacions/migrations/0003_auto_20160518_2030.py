# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

migrate_user_sql = '''
INSERT INTO comptes_usuari
    ( id, password, last_login, is_superuser, email,
      nom, cognoms,
      is_staff, is_active, date_joined )
    SELECT a.id, a.password, a.last_login, a.is_superuser, a.email,
           a.first_name, a.last_name, a.is_staff, a.is_active, a.date_joined
    FROM auth_user `a`
'''

migrate_user_groups_sql = '''
INSERT INTO comptes_usuari_groups ( id, usuari_id, group_id )
    SELECT a.id, a.user_id, a.group_id FROM auth_user_groups `a`
'''

class Migration(migrations.Migration):

    dependencies = [
        ('publicacions', '0002_auto_20150611_1554'),
    ]

    operations = [
        migrations.RunSQL(migrate_user_sql),
        migrations.RunSQL(migrate_user_groups_sql),
    ]
