from .models import Artist
from django.shortcuts import render
# from django.views.generic import ListView
from django.views.generic.detail import DetailView

class ArtistDetailView(DetailView):
	model = Artist;
	#atibuto
	context_object_name = 'artist';
	def get_template_names(self):
		return 'artists.html';

# class ArtistListView(ListView):
# 	model = Artist;
# 	context_object_name = 'artists';
# 	template_name = 'artists.html'	


#en ves de crear una vista tiene multiples vistas creadas
from rest_framework import viewsets
from .serializers import ArtistSerializer

class ArtistViewSet(viewsets.ModelViewSet):
	model = Artist;
	serializer_class = ArtistSerializer;
	filter_fields = ('id',)
	paginate_by = 1;

