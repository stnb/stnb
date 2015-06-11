# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import stnb.seminaris.models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacions', '0001_initial'),
        ('membres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField(verbose_name='date')),
            ],
            options={
                'ordering': ['seminari__data_inici', 'data'],
                'verbose_name': 'day',
                'verbose_name_plural': 'days',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DiaTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='seminaris.Dia', null=True)),
            ],
            options={
                'db_table': 'seminaris_dia_translation',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ItemPrograma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hora_inici', models.TimeField(verbose_name='start time')),
                ('hora_finalizacio', models.TimeField(verbose_name='end time')),
                ('dia', models.ForeignKey(related_name='items_programa', verbose_name='day', to='seminaris.Dia')),
            ],
            options={
                'ordering': ['dia', 'hora_inici'],
                'verbose_name': 'programme item',
                'verbose_name_plural': 'programme items',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ItemProgramaTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcio', models.CharField(help_text="Only necessary if a talk isn't chosen.", max_length=255, null=True, verbose_name='description', blank=True)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='seminaris.ItemPrograma', null=True)),
            ],
            options={
                'db_table': 'seminaris_itemprograma_translation',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Seminari',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(verbose_name='slug')),
                ('data_inici', models.DateField(verbose_name='start date')),
                ('data_finalizacio', models.DateField(verbose_name='end date')),
                ('altres_organitzadors', models.CharField(max_length=250, null=True, verbose_name='other organisers', blank=True)),
                ('enllac_inscripcio', models.CharField(max_length=250, null=True, verbose_name='registration form', blank=True)),
                ('programa_pdf', models.FileField(upload_to=b'seminaris/programes', null=True, verbose_name='programme PDF', blank=True)),
                ('actiu', models.BooleanField(default=False, verbose_name='active')),
                ('organitzadors', models.ManyToManyField(related_name='seminaris', null=True, verbose_name='organisers', to='membres.Membre', blank=True)),
                ('publicacio', models.ForeignKey(related_name='seminaris', verbose_name='publication', blank=True, to='publicacions.Publicacio', null=True)),
            ],
            options={
                'ordering': ['-data_inici'],
                'verbose_name': 'seminar',
                'verbose_name_plural': 'seminars',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SeminariTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=50, verbose_name='name')),
                ('lloc', models.TextField(verbose_name='location')),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='seminaris.Seminari', null=True)),
            ],
            options={
                'db_table': 'seminaris_seminari_translation',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ordre', models.IntegerField(default=0, verbose_name='order')),
                ('altres_organitzadors', models.CharField(max_length=250, null=True, verbose_name='other organisers', blank=True)),
                ('referencies', models.TextField(null=True, verbose_name='references', blank=True)),
                ('organitzadors', models.ManyToManyField(related_name='temes', null=True, verbose_name='organisers', to='membres.Membre', blank=True)),
                ('publicacio', models.ForeignKey(related_name='temes', verbose_name='publication', blank=True, to='publicacions.Publicacio', null=True)),
                ('seminari', models.ForeignKey(related_name='temes', verbose_name='seminar', to='seminaris.Seminari')),
            ],
            options={
                'ordering': ['seminari', 'ordre'],
                'verbose_name': 'theme',
                'verbose_name_plural': 'themes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TemaTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titol', models.CharField(max_length=255, verbose_name='title')),
                ('descripcio', models.TextField(null=True, verbose_name='description', blank=True)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='seminaris.Tema', null=True)),
            ],
            options={
                'db_table': 'seminaris_tema_translation',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Xerrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ordre', models.IntegerField(default=0, verbose_name='order')),
                ('altres_presentadors', models.CharField(max_length=250, null=True, verbose_name='other presenters', blank=True)),
                ('presentacio', models.FileField(upload_to=stnb.seminaris.models.presentacio_nom_fitxer, null=True, verbose_name='presentation', blank=True)),
                ('article', models.FileField(upload_to=stnb.seminaris.models.article_nom_fitxer, null=True, verbose_name='article', blank=True)),
                ('presentadors', models.ManyToManyField(related_name='xerrades', null=True, verbose_name='presenters', to='membres.Membre', blank=True)),
                ('tema', models.ForeignKey(related_name='xerrades', verbose_name='theme', blank=True, to='seminaris.Tema', null=True)),
            ],
            options={
                'ordering': ['tema', 'ordre'],
                'verbose_name': 'talk',
                'verbose_name_plural': 'talks',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='XerradaTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titol', models.CharField(max_length=255, verbose_name='title')),
                ('abstracte', models.TextField(null=True, verbose_name='abstract', blank=True)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='seminaris.Xerrada', null=True)),
            ],
            options={
                'db_table': 'seminaris_xerrada_translation',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='xerradatranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='tematranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='seminaritranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='itemprogramatranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AddField(
            model_name='itemprograma',
            name='xerrada',
            field=models.ForeignKey(related_name='items_programa', verbose_name='talk', blank=True, to='seminaris.Xerrada', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='diatranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AddField(
            model_name='dia',
            name='seminari',
            field=models.ForeignKey(related_name='dies', verbose_name='seminar', to='seminaris.Seminari'),
            preserve_default=True,
        ),
    ]
