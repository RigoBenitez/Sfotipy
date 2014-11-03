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

# --------------------------------------para cache-------------------------------------------
from django.contrib.sessions.models import Session 
from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

# se puede agregar a caulquier modelo
#se deve ejecutar siemre despues de que se grave un modelo
# @receiver(post_save)
# def clear_cache(sender, **kwargs):
# 	# si el modelo que lo envia(artist, album, etc) se actualiza y no es una sesion
# 	# borre el cache, cada que grabamos un modelo 
# 	if sender != Session:
# 		cache._cache.flush_all();
