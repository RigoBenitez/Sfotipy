from django.contrib import admin
from .models import Album
from sorl.thumbnail import get_thumbnail

class AlbumAdmin(admin.ModelAdmin):
	list_display = ('title', 'imageAlbum', )

	#obj es el elemneto de la lista que vamos a iterar
	def imageAlbum(self, obj):
		return ' <img src="%s" alt="" /> ' % get_thumbnail(obj.cover, '100x100').url;

	imageAlbum.allow_tags = True;


admin.site.register(Album, AlbumAdmin);

