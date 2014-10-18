from django.contrib import admin
from .models import Track

class TrackAdmin(admin.ModelAdmin):
	list_display = ('title', 'artist', 'order','album', 'player');
	list_filter = ('artist', 'album');
	search_fields = ('title', 'artist__firstName')


admin.site.register(Track, TrackAdmin);
