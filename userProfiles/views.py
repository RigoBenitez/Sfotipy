from .forms import UserCreationEmailForm, EmailAutheticationForm
from django.contrib.auth import login
from django.shortcuts import render

def signup(request):
	#Este formulario se cree con estos datos si hay datos post entonces llene este formulario y creelo con el formulario
	form = UserCreationEmailForm(request.POST or None);

	if form.is_valid():
		form.save(); #se guarda en un usuario

	return render(request, 'signup.html', {'form': form});

def signin(request):
	form = EmailAutheticationForm(request.POST or None);

	if form.is_valid():
		login(request, form.get_user());

	return render(request, 'signin.html', {'form': form} );