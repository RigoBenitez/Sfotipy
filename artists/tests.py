from django.test import TestCase
from .models import Artist
from tracks.models import Track
from albums.models import Album


#pruebas basicas de siempre
class TestArtist(TestCase):
	#siempre hay un setUp
	def setUp(self):
		#Crea un artista
		self.artist = Artist.objects.create(firstName='jose', lastName='pachuco');
		self.album = Album.objects.create(title='hola', artirts=self.artist);
		self.track = Track.objects.create(title='hola', order=8, trackFile='/as/', album=self.album, artist=self.artist);

	def testExisteVista(self):
		#client permite hacer request a nuestra pagina y probar que si sirve
		res = self.client.get('/artists/%d' % self.artist.id);
		#verifica elestado 200 y david en la respuesta
		self.assertEqual(res.status_code, 200);
		self.assertTrue('jose' in res.content);
	
	def test404(self):
		id_viejo = self.artist.id;
		self.artist.delete();
		res = self.client.get('/artists/%d' % id_viejo);
		self.assertEqual(res.status_code, 404);
	
	def testLogIn(self):
		res = self.client.get('/tracks/%s' % self.track.title);
		#302 es de redireccion si hay un @login_requiered en la vista 
		#redirige y no lo deja entrar a los tracks
		self.assertEqual(res.status_code, 302);
