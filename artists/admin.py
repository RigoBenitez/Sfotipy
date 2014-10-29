from django.contrib import admin
from .models import Artist
from tracks.models import Track
from albums.models import Album

class TrackInline(admin.StackedInline):
	model = Track;
	#solo mostrar un extra
	extra = 1;


class AlbumInline(admin.StackedInline):
	model = Album;
	extra = 1;

#Administrado dentro del admin de django
#solo un nivel de inline
class ArtistAdmin(admin.ModelAdmin):
	#los filter hacen que los many to many se vean mejor
	filter_horizontal = ('favoriteSongs',)
	#filter_vertical = ('favoriteSongs',)
	inlines = [TrackInline, AlbumInline]
	search_fields = ('firstName', );


admin.site.register(Artist, ArtistAdmin);

