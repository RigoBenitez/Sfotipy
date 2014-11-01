#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from artists.models import Artist

class Album(models.Model):
	title = models.CharField(max_length=255);
	cover = models.ImageField(upload_to='albums');
	artirts = models.ForeignKey(Artist); #Se especifica que artista es
	
	def __unicode__(self):
		return self.title;