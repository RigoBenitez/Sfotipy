#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .models import Track
from albums.models import Album 
from django.contrib.auth.decorators import login_required
#para usar el cache con redis
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
import json
import time



# If the user isn’t logged in, redirect to settings.LOGIN_URL, 
# passing the current absolute path in the query string
# @login_required

#se guarda por 60 segundos
@cache_page(10)

def trackView(request, title):
	track = get_object_or_404(Track, title = title);
	bio = track.artist.biography;
	# album = Album.objects.all(); #devuelve los objetos de Album
	# import ipdb; ipdb.set_trace()
	
	'''
	try:
		track = Track.objects.get(title = title);
	except Track.DoesNotExist:
		raise Http404
	'''

	# data es lo que sale del cache
	# data  = cache.get('data_%s' % title);

	# if data is None:
	data = {
		'title': track.title,
		'order': track.order,
		'album': track.album.title,
		'artist': {
			'name': track.artist.firstName,
			'bio': bio,
		}
	}
	# time.sleep(5)
		# se serializa el diccionario de data
		# cache.set('data_%s' % title, data);

	#con loads haces lo contrario
	# json_data = json.dumps(data);
	# return HttpResponse(json_data, content_type='application/json');
	return render(request, 'track.html', {'track': track, 'bio': bio,});

# from .models import Artist
# from artists.serializers import ArtistSerializer
from rest_framework import viewsets

class TrackViewSet(viewsets.ModelViewSet):
	model = Track;
