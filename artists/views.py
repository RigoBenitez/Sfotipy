from django.shortcuts import render
from .models import Artist
from django.views.generic.detail import DetailView

class ArtistDetailView(DetailView):
	model = Artist;
	#atibuto
	context_object_name = 'artist';
	def get_template_names(self):
		return 'artists.html';
