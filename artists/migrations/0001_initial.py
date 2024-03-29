# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artist'
        db.create_table(u'artists_artist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('biography', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'artists', ['Artist'])

        # Adding M2M table for field favoriteSongs on 'Artist'
        m2m_table_name = db.shorten_name(u'artists_artist_favoriteSongs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('artist', models.ForeignKey(orm[u'artists.artist'], null=False)),
            ('track', models.ForeignKey(orm[u'tracks.track'], null=False))
        ))
        db.create_unique(m2m_table_name, ['artist_id', 'track_id'])


    def backwards(self, orm):
        # Deleting model 'Artist'
        db.delete_table(u'artists_artist')

        # Removing M2M table for field favoriteSongs on 'Artist'
        db.delete_table(db.shorten_name(u'artists_artist_favoriteSongs'))


    models = {
        u'albums.album': {
            'Meta': {'object_name': 'Album'},
            'artirts': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artists.Artist']"}),
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'artists.artist': {
            'Meta': {'object_name': 'Artist'},
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'favoriteSongs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'is_favorite_of'", 'blank': 'True', 'to': u"orm['tracks.Track']"}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'tracks.track': {
            'Meta': {'object_name': 'Track'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['albums.Album']"}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artists.Artist']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'trackFile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['artists']