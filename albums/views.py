from .models import Album
from django.shortcuts import render
from rest_framework import viewsets

class AlbumViewSet(viewsets.ModelViewSet):
	model = Album