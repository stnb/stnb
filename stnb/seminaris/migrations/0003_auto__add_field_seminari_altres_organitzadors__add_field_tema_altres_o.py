# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Seminari.altres_organitzadors'
        db.add_column('seminaris_seminari', 'altres_organitzadors',
                      self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Tema.altres_organitzadors'
        db.add_column('seminaris_tema', 'altres_organitzadors',
                      self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Xerrada.altres_presentadors'
        db.alter_column('seminaris_xerrada', 'altres_presentadors', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

    def backwards(self, orm):
        # Deleting field 'Seminari.altres_organitzadors'
        db.delete_column('seminaris_seminari', 'altres_organitzadors')

        # Deleting field 'Tema.altres_organitzadors'
        db.delete_column('seminaris_tema', 'altres_organitzadors')


        # Changing field 'Xerrada.altres_presentadors'
        db.alter_column('seminaris_xerrada', 'altres_presentadors', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

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
            'altres_organitzadors': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
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
            'altres_organitzadors': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordre': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'organitzadors': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'temes'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['membres.Membre']"}),
            'referencies': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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
            'altres_presentadors': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
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