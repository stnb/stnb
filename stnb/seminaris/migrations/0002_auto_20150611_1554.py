# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seminaris', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diatranslation',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='itemprogramatranslation',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='seminaritranslation',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tematranslation',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='xerradatranslation',
            options={'managed': True},
        ),
        migrations.AlterField(
            model_name='seminari',
            name='organitzadors',
            field=models.ManyToManyField(related_name='seminaris', verbose_name='organisers', to='membres.Membre', blank=True),
        ),
        migrations.AlterField(
            model_name='tema',
            name='organitzadors',
            field=models.ManyToManyField(related_name='temes', verbose_name='organisers', to='membres.Membre', blank=True),
        ),
        migrations.AlterField(
            model_name='xerrada',
            name='presentadors',
            field=models.ManyToManyField(related_name='xerrades', verbose_name='presenters', to='membres.Membre', blank=True),
        ),
    ]
