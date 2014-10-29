from django.test import TestCase
from .models import Artist


#pueba sencilla 
class TestArtist(TestCase):
	#siempre hay un setUp
	def setUp(self):
		#Crea un artista
		self.artist = Artist.objects.create(firstName='jose jose', lastName='pachuco');

	def testExisteVista(self):
		#client permite hacer request a nuestra pagina y probar que si sirve
		print self.client.get('/artists/%d' % self.artist.id);
		#pruebas basicasde siempre
		#verifica elestado 200 y david en la respuesta

		# self.assertEqual(res.status_code, 200);
		# self.assertTrue('david' in res.content);
