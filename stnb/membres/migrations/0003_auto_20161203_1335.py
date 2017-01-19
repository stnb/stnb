# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membres', '0002_auto_20150611_1554'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='membretranslation',
            options={'default_permissions': (), 'managed': True},
        ),
        migrations.AlterField(
            model_name='membretranslation',
            name='master',
            field=models.ForeignKey(related_name='translations', editable=False, to='membres.Membre'),
        ),
    ]
