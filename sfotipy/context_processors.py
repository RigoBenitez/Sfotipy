from random import choice
from tracks.models import Track

# Recibe un request y regresa un diccionario
frases = ['lol', 'hola amigos', 'la caca de perro es buena', 'python es tu padre'];

def basico(request):
	tracks = Track.objects.all()
	# import ipdb; ipdb.set_trace()
	track  = None
	for t in tracks:
		#request.path es le ruta que pone el usuario
		if request.path == t.get_absolute_url():
			track = t;
			break;
	return {'titulo': choice(frases), 'tracks': tracks, 'selected_track': track}