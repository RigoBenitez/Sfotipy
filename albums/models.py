from django.db import models
from artists.models import Artist

class Album(models.Model):
	title = models.CharField(max_length=255);
	cover = models.ImageField(upload_to='albums');
	artirts = models.ForeignKey(Artist); #Se especifica que artista es