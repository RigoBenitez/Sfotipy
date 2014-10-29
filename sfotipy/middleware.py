from random import choice
from django.shortcuts import redirect

paises = ['Mexico', 'Colombia', 'Brazil'];

def paisDeOrigen(request):
	#decide el pais aleatoriamente
	return choice(paises);

class PaisMiddleware():
	#antes de que llegue a la vista 
	def process_request(self, request):
		pais = paisDeOrigen(request);
		if pais == 'Mexico':
			return redirect('http://mejorando.la/');