#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from albums.models import Album 
from django.contrib.auth.decorators import login_required
from .models import Track

# If the user isn’t logged in, redirect to settings.LOGIN_URL, 
# passing the current absolute path in the query string
@login_required

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
	
	data = {
		'title': track.title,
		'order': track.order,
		'album': track.album.title,
		'artist': {
			'name': track.artist.firstName,
			'bio': bio,
		}
	}

	#con loads haces lo contrario
	# json_data = json.dumps(data);
	# return HttpResponse(json_data, content_type='application/json');
	return render(request, 'track.html', {'track': track, 'bio': bio,});

from .models import Artist
from artists.serializers import ArtistSerializer
from rest_framework import viewsets

class TrackViewSet(viewsets.ModelViewSet):
	model = Track;
