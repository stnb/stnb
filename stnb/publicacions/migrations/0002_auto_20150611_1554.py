# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicacions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publicaciotranslation',
            options={'managed': True},
        ),
        migrations.AlterField(
            model_name='publicacio',
            name='autors',
            field=models.ManyToManyField(related_name='publicacions', verbose_name='authors', to='membres.Membre', blank=True),
        ),
        migrations.AlterField(
            model_name='publicacio',
            name='editors',
            field=models.ManyToManyField(related_name='publicacions_editades', verbose_name='editors', to='membres.Membre', blank=True),
        ),
    ]
