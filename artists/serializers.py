#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .models import Artist
from rest_framework import serializers 

#cuando encuentre una referencia a este modelo va a agregar un enlace a el
class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	es_metalica_1 = serializers.SerializerMethodField('es_metallica_2')

	def es_metallica_2(self, obj):
		return obj.es_metallica()

	class Meta:
		model = Artist;
		#limitar información que sale de nuestra base de datos
		fields = ('firstName', 'lastName', 'es_metalica_1')
