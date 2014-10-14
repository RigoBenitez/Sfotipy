from django.db import models

class Artist(models.Model):
	firstName = models.CharField(max_length=255);
	lastName  = models.CharField(max_length=255, blank=True);
	biography =models.TextField(blank=True); #TextField es un textarea en el html
	
	def __unicode__(self):
		return self.firstName; 