from django.contrib import admin
from .models import Artist
from tracks.models import Track
from albums.models import Album

class TrackInline(admin.StackedInline):
	model = Track;
	extra = 1;


class AlbumInline(admin.StackedInline):
	model = Album;
	extra = 1;

class ArtistAdmin(admin.ModelAdmin):
	filter_horizontal = ('favoriteSongs',)
	#filter_vertical = ('favoriteSongs',)
	inlines = [AlbumInline, TrackInline]
	search_fields = ('firstName', );


admin.site.register(Artist, ArtistAdmin);

