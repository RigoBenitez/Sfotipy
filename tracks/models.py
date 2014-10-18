from django.db import models
from albums.models import Album
from artists.models import Artist

class Track(models.Model):
	title = models.CharField(max_length=255);
	order = models.PositiveIntegerField();
	trackFile = models.FileField(upload_to='tracks');
	album = models.ForeignKey(Album);
	artist = models.ForeignKey(Artist);

	def player(self):
		return """
		<audio controls>
			<source src="%s" type="audio/mpeg">
			Tu browser es basura
		</audio>
		""" % self.trackFile.url
	player.allow_tags = True;

	def __unicode__(self):
		return self.title;