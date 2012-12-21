# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SeminariTranslation'
        db.create_table('seminaris_seminari_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('lloc', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['seminaris.Seminari'])),
        ))
        db.send_create_signal('seminaris', ['SeminariTranslation'])

        # Adding unique constraint on 'SeminariTranslation', fields ['language_code', 'master']
        db.create_unique('seminaris_seminari_translation', ['language_code', 'master_id'])

        # Adding model 'Seminari'
        db.create_table('seminaris_seminari', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('data_inici', self.gf('django.db.models.fields.DateField')()),
            ('data_finalizacio', self.gf('django.db.models.fields.DateField')()),
            ('actiu', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('seminaris', ['Seminari'])

        # Adding M2M table for field organitzadors on 'Seminari'
        db.create_table('seminaris_seminari_organitzadors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('seminari', models.ForeignKey(orm['seminaris.seminari'], null=False)),
            ('membre', models.ForeignKey(orm['membres.membre'], null=False))
        ))
        db.create_unique('seminaris_seminari_organitzadors', ['seminari_id', 'membre_id'])

        # Adding model 'TemaTranslation'
        db.create_table('seminaris_tema_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titol', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('descripcio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['seminaris.Tema'])),
        ))
        db.send_create_signal('seminaris', ['TemaTranslation'])

        # Adding unique constraint on 'TemaTranslation', fields ['language_code', 'master']
        db.create_unique('seminaris_tema_translation', ['language_code', 'master_id'])

        # Adding model 'Tema'
        db.create_table('seminaris_tema', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seminari', self.gf('django.db.models.fields.related.ForeignKey')(related_name='temes', to=orm['seminaris.Seminari'])),
            ('ordre', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('seminaris', ['Tema'])

        # Adding M2M table for field organitzadors on 'Tema'
        db.create_table('seminaris_tema_organitzadors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tema', models.ForeignKey(orm['seminaris.tema'], null=False)),
            ('membre', models.ForeignKey(orm['membres.membre'], null=False))
        ))
        db.create_unique('seminaris_tema_organitzadors', ['tema_id', 'membre_id'])

        # Adding model 'DiaTranslation'
        db.create_table('seminaris_dia_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['seminaris.Dia'])),
        ))
        db.send_create_signal('seminaris', ['DiaTranslation'])

        # Adding unique constraint on 'DiaTranslation', fields ['language_code', 'master']
        db.create_unique('seminaris_dia_translation', ['language_code', 'master_id'])

        # Adding model 'Dia'
        db.create_table('seminaris_dia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data', self.gf('django.db.models.fields.DateField')()),
            ('seminari', self.gf('django.db.models.fields.related.ForeignKey')(related_name='dies', to=orm['seminaris.Seminari'])),
        ))
        db.send_create_signal('seminaris', ['Dia'])

        # Adding model 'XerradaTranslation'
        db.create_table('seminaris_xerrada_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titol', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('abstracte', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['seminaris.Xerrada'])),
        ))
        db.send_create_signal('seminaris', ['XerradaTranslation'])

        # Adding unique constraint on 'XerradaTranslation', fields ['language_code', 'master']
        db.create_unique('seminaris_xerrada_translation', ['language_code', 'master_id'])

        # Adding model 'Xerrada'
        db.create_table('seminaris_xerrada', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tema', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='xerrades', null=True, to=orm['seminaris.Tema'])),
            ('ordre', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('altres_presentadors', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('presentacio', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('article', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('seminaris', ['Xerrada'])

        # Adding M2M table for field presentadors on 'Xerrada'
        db.create_table('seminaris_xerrada_presentadors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('xerrada', models.ForeignKey(orm['seminaris.xerrada'], null=False)),
            ('membre', models.ForeignKey(orm['membres.membre'], null=False))
        ))
        db.create_unique('seminaris_xerrada_presentadors', ['xerrada_id', 'membre_id'])

        # Adding model 'ItemProgramaTranslation'
        db.create_table('seminaris_itemprograma_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcio', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['seminaris.ItemPrograma'])),
        ))
        db.send_create_signal('seminaris', ['ItemProgramaTranslation'])

        # Adding unique constraint on 'ItemProgramaTranslation', fields ['language_code', 'master']
        db.create_unique('seminaris_itemprograma_translation', ['language_code', 'master_id'])

        # Adding model 'ItemPrograma'
        db.create_table('seminaris_itemprograma', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('xerrada', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='items_programa', null=True, to=orm['seminaris.Xerrada'])),
            ('dia', self.gf('django.db.models.fields.related.ForeignKey')(related_name='items_programa', to=orm['seminaris.Dia'])),
            ('hora_inici', self.gf('django.db.models.fields.TimeField')()),
            ('hora_finalizacio', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('seminaris', ['ItemPrograma'])


    def backwards(self, orm):
        # Removing unique constraint on 'ItemProgramaTranslation', fields ['language_code', 'master']
        db.delete_unique('seminaris_itemprograma_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'XerradaTranslation', fields ['language_code', 'master']
        db.delete_unique('seminaris_xerrada_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'DiaTranslation', fields ['language_code', 'master']
        db.delete_unique('seminaris_dia_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'TemaTranslation', fields ['language_code', 'master']
        db.delete_unique('seminaris_tema_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'SeminariTranslation', fields ['language_code', 'master']
        db.delete_unique('seminaris_seminari_translation', ['language_code', 'master_id'])

        # Deleting model 'SeminariTranslation'
        db.delete_table('seminaris_seminari_translation')

        # Deleting model 'Seminari'
        db.delete_table('seminaris_seminari')

        # Removing M2M table for field organitzadors on 'Seminari'
        db.delete_table('seminaris_seminari_organitzadors')

        # Deleting model 'TemaTranslation'
        db.delete_table('seminaris_tema_translation')

        # Deleting model 'Tema'
        db.delete_table('seminaris_tema')

        # Removing M2M table for field organitzadors on 'Tema'
        db.delete_table('seminaris_tema_organitzadors')

        # Deleting model 'DiaTranslation'
        db.delete_table('seminaris_dia_translation')

        # Deleting model 'Dia'
        db.delete_table('seminaris_dia')

        # Deleting model 'XerradaTranslation'
        db.delete_table('seminaris_xerrada_translation')

        # Deleting model 'Xerrada'
        db.delete_table('seminaris_xerrada')

        # Removing M2M table for field presentadors on 'Xerrada'
        db.delete_table('seminaris_xerrada_presentadors')

        # Deleting model 'ItemProgramaTranslation'
        db.delete_table('seminaris_itemprograma_translation')

        # Deleting model 'ItemPrograma'
        db.delete_table('seminaris_itemprograma')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'institucions.institucio': {
            'Meta': {'object_name': 'Institucio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nom_curt': ('django.db.models.fields.SlugField', [], {'max_length': '10'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'membres.membre': {
            'Meta': {'ordering': "['cognoms', 'nom']", 'object_name': 'Membre'},
            'afiliacio': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'membres'", 'null': 'True', 'to': "orm['institucions.Institucio']"}),
            'amagar_perfil': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cognoms': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'membre_actual': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'membre_des_de': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '160', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'seminaris.dia': {
            'Meta': {'ordering': "['seminari__data_inici', 'data']", 'object_name': 'Dia'},
            'data': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seminari': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dies'", 'to': "orm['seminaris.Seminari']"})
        },
        'seminaris.diatranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'DiaTranslation', 'db_table': "'seminaris_dia_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['seminaris.Dia']"})
        },
        'seminaris.itemprograma': {
            'Meta': {'ordering': "['dia', 'hora_inici']", 'object_name': 'ItemPrograma'},
            'dia': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items_programa'", 'to': "orm['seminaris.Dia']"}),
            'hora_finalizacio': ('django.db.models.fields.TimeField', [], {}),
            'hora_inici': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'xerrada': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'items_programa'", 'null': 'True', 'to': "orm['seminaris.Xerrada']"})
        },
        'seminaris.itemprogramatranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'ItemProgramaTranslation', 'db_table': "'seminaris_itemprograma_translation'"},
            'descripcio': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['seminaris.ItemPrograma']"})
        },
        'seminaris.seminari': {
            'Meta': {'ordering': "['-data_inici']", 'object_name': 'Seminari'},
            'actiu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'data_finalizacio': ('django.db.models.fields.DateField', [], {}),
            'data_inici': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organitzadors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'seminaris'", 'symmetrical': 'False', 'to': "orm['membres.Membre']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'seminaris.seminaritranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'SeminariTranslation', 'db_table': "'seminaris_seminari_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'lloc': ('django.db.models.fields.TextField', [], {}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['seminaris.Seminari']"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'seminaris.tema': {
            'Meta': {'ordering': "['seminari', 'ordre']", 'object_name': 'Tema'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordre': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'organitzadors': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'temes'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['membres.Membre']"}),
            'seminari': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'temes'", 'to': "orm['seminaris.Seminari']"})
        },
        'seminaris.tematranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'TemaTranslation', 'db_table': "'seminaris_tema_translation'"},
            'descripcio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['seminaris.Tema']"}),
            'titol': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'seminaris.xerrada': {
            'Meta': {'ordering': "['tema', 'ordre']", 'object_name': 'Xerrada'},
            'altres_presentadors': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'article': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordre': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'presentacio': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'presentadors': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'xerrades'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['membres.Membre']"}),
            'tema': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'xerrades'", 'null': 'True', 'to': "orm['seminaris.Tema']"})
        },
        'seminaris.xerradatranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'XerradaTranslation', 'db_table': "'seminaris_xerrada_translation'"},
            'abstracte': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['seminaris.Xerrada']"}),
            'titol': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['seminaris']