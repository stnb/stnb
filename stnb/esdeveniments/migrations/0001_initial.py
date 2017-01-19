# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import stnb.esdeveniments.models


class Migration(migrations.Migration):

    dependencies = [
        ('membres', '0003_auto_20161203_1335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Esdeveniment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(max_length=100, verbose_name='slug', blank=True)),
                ('data', models.DateField(verbose_name='date')),
                ('hora_inici', models.TimeField(null=True, verbose_name='start time', blank=True)),
                ('hora_finalizacio', models.TimeField(null=True, verbose_name='end time', blank=True)),
                ('altres_amfitrions', models.CharField(max_length=250, null=True, verbose_name='other hosts', blank=True)),
                ('altres_presentadors', models.CharField(max_length=250, null=True, verbose_name='other presenters', blank=True)),
                ('presentacio', models.FileField(upload_to=stnb.esdeveniments.models.presentacio_nom_fitxer, null=True, verbose_name='presentation', blank=True)),
                ('article', models.FileField(upload_to=stnb.esdeveniments.models.article_nom_fitxer, null=True, verbose_name='article', blank=True)),
                ('amfitrions', models.ManyToManyField(related_name='esdeveniments_organizats', verbose_name='hosts', to='membres.Membre', blank=True)),
                ('presentadors', models.ManyToManyField(related_name='esdeveniments_presentats', verbose_name='presenters', to='membres.Membre', blank=True)),
            ],
            options={
                'ordering': ['-data'],
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
        ),
        migrations.CreateModel(
            name='EsdevenimentTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titol', models.CharField(max_length=255, verbose_name='title')),
                ('abstracte', models.TextField(null=True, verbose_name='abstract', blank=True)),
                ('lloc', models.TextField(null=True, verbose_name='location', blank=True)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='esdeveniments.Esdeveniment')),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'esdeveniments_esdeveniment_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(verbose_name='slug', blank=True)),
                ('altres_organitzadors', models.CharField(max_length=250, null=True, verbose_name='other organisers', blank=True)),
                ('organitzadors', models.ManyToManyField(related_name='series', verbose_name='organisers', to='membres.Membre', blank=True)),
            ],
            options={
                'verbose_name': 'series',
                'verbose_name_plural': 'series',
            },
        ),
        migrations.CreateModel(
            name='SerieTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=50, verbose_name='name')),
                ('descripcio', models.TextField(null=True, verbose_name='description', blank=True)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='esdeveniments.Serie')),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'esdeveniments_serie_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.AddField(
            model_name='esdeveniment',
            name='serie',
            field=models.ForeignKey(related_name='esdeveniments', verbose_name='serie', blank=True, to='esdeveniments.Serie', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='serietranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='esdevenimenttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
