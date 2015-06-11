# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('membres', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='membretranslation',
            options={'managed': True},
        ),
        migrations.AlterField(
            model_name='membre',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
