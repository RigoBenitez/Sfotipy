from django.db import models

class Artist(models.Model):
	firstName = models.CharField(max_length=255);
	lastName  = models.CharField(max_length=255, blank=True);
	biography =models.TextField(blank=True); #TextField es un textarea en el html
	favoriteSongs = models.ManyToManyField('tracks.Track', blank=True, related_name='is_favorite_of');
	
	def es_metallica(self):
		return self.pk == 1

	# @staticmethod
	def autocomplete_serch_fields():
		return ("id__iexact", "firstName__icontains", "lastName__icontains");

	def __unicode__(self):
		return self.firstName; 
