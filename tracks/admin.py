from django.contrib import admin
from .models import Track

class TrackAdmin(admin.ModelAdmin):
	list_display = ('artist', 'title', 'order','album', 'player', 'es_metallica');
	list_filter = ('artist', 'album');
	search_fields = ('title', 'artist__firstName');
	list_editable = ('title', 'album');
	#actions = (export_as_excel);
	raw_id_fields = ('artist', )

	def es_metallica(self, obj):
		#obj recibe todos los objetos
		return obj.id == 1;	
	#Pone un palomita cuando se encuentrea acdc con 
	es_metallica.boolean = True;

admin.site.register(Track, TrackAdmin);
