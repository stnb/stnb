# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import stnb.publicacions.models


class Migration(migrations.Migration):

    dependencies = [
        ('membres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('altres_autors', models.CharField(max_length=250, null=True, verbose_name='other authors', blank=True)),
                ('altres_editors', models.CharField(max_length=250, null=True, verbose_name='other editors', blank=True)),
                ('isbn', models.CharField(max_length=20, null=True, verbose_name=b'ISBN', blank=True)),
                ('data_publicacio', models.DateField(help_text='Only the month and year are displayed', null=True, verbose_name='publication date', blank=True)),
                ('fitxer', models.FileField(upload_to=stnb.publicacions.models.publicacio_nom_fitxer, null=True, verbose_name='file', blank=True)),
                ('autors', models.ManyToManyField(related_name='publicacions', null=True, verbose_name='authors', to='membres.Membre', blank=True)),
                ('editors', models.ManyToManyField(related_name='publicacions_editades', null=True, verbose_name='editors', to='membres.Membre', blank=True)),
            ],
            options={
                'ordering': ['data_publicacio'],
                'verbose_name': 'publication',
                'verbose_name_plural': 'publicacions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicacioTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(help_text='Publication name', max_length=128, verbose_name='name')),
                ('descripcio', models.CharField(help_text='A short description.', max_length=255, null=True, verbose_name='description', blank=True)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='publicacions.Publicacio', null=True)),
            ],
            options={
                'db_table': 'publicacions_publicacio_translation',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='publicaciotranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
