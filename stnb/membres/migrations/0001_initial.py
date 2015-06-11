# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('institucions', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=50, null=True, verbose_name='name')),
                ('cognoms', models.CharField(max_length=100, null=True, verbose_name='surname')),
                ('slug', models.SlugField(unique=True, max_length=160, blank=True)),
                ('foto', models.ImageField(upload_to=b'membres/fotos/', null=True, verbose_name='photo', blank=True)),
                ('enllac', models.CharField(max_length=250, null=True, verbose_name='link', blank=True)),
                ('membre_des_de', models.IntegerField(null=True, verbose_name='member since', blank=True)),
                ('membre_actual', models.BooleanField(default=True, verbose_name='current member')),
                ('amagar_perfil', models.BooleanField(default=False, verbose_name='hide profile')),
                ('afiliacio', models.ForeignKey(related_name='membres', verbose_name='affiliation', blank=True, to='institucions.Institucio', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'ordering': ['cognoms', 'nom'],
                'verbose_name': 'member',
                'verbose_name_plural': 'members',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MembreTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(null=True, verbose_name='biography', blank=True)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='membres.Membre', null=True)),
            ],
            options={
                'db_table': 'membres_membre_translation',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='membretranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
