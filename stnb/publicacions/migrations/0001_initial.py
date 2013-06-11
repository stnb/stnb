# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PublicacioTranslation'
        db.create_table('publicacions_publicacio_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('descripcio', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['publicacions.Publicacio'])),
        ))
        db.send_create_signal('publicacions', ['PublicacioTranslation'])

        # Adding unique constraint on 'PublicacioTranslation', fields ['language_code', 'master']
        db.create_unique('publicacions_publicacio_translation', ['language_code', 'master_id'])

        # Adding model 'Publicacio'
        db.create_table('publicacions_publicacio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('altres_autors', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('altres_editors', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('data_publicacio', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fitxer', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('publicacions', ['Publicacio'])

        # Adding M2M table for field autors on 'Publicacio'
        db.create_table('publicacions_publicacio_autors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('publicacio', models.ForeignKey(orm['publicacions.publicacio'], null=False)),
            ('membre', models.ForeignKey(orm['membres.membre'], null=False))
        ))
        db.create_unique('publicacions_publicacio_autors', ['publicacio_id', 'membre_id'])

        # Adding M2M table for field editors on 'Publicacio'
        db.create_table('publicacions_publicacio_editors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('publicacio', models.ForeignKey(orm['publicacions.publicacio'], null=False)),
            ('membre', models.ForeignKey(orm['membres.membre'], null=False))
        ))
        db.create_unique('publicacions_publicacio_editors', ['publicacio_id', 'membre_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'PublicacioTranslation', fields ['language_code', 'master']
        db.delete_unique('publicacions_publicacio_translation', ['language_code', 'master_id'])

        # Deleting model 'PublicacioTranslation'
        db.delete_table('publicacions_publicacio_translation')

        # Deleting model 'Publicacio'
        db.delete_table('publicacions_publicacio')

        # Removing M2M table for field autors on 'Publicacio'
        db.delete_table('publicacions_publicacio_autors')

        # Removing M2M table for field editors on 'Publicacio'
        db.delete_table('publicacions_publicacio_editors')


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
            'enllac': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'membre_actual': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'membre_des_de': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '160', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'publicacions.publicacio': {
            'Meta': {'ordering': "['data_publicacio']", 'object_name': 'Publicacio'},
            'altres_autors': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'altres_editors': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'autors': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'publicacions'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['membres.Membre']"}),
            'data_publicacio': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'editors': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'publicacions_editades'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['membres.Membre']"}),
            'fitxer': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        'publicacions.publicaciotranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'PublicacioTranslation', 'db_table': "'publicacions_publicacio_translation'"},
            'descripcio': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['publicacions.Publicacio']"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['publicacions']