from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 	

class UserCreationEmailForm(UserCreationForm):
	email = forms.EmailField(); #django valida si es un email

	class Meta:
		model = User;
		fields = ('username', 'email');

class EmailAutheticationForm(forms.Form):
	email = forms.EmailField();
	password = forms.CharField(label='Password', widget=forms.PasswordInput);

	def __init__(self, *args, **kwargs):
		#el usuario que voy a tratar de validar primero va  
		#a ser None despues de que recibo datos trato de autenticarlo
		self.user_cache = None;
		#inicializa l padre
		super(EmailAutheticationForm, self).__init__(*args, **kwargs);

	def clean(self):
		#Traigo el dato del email y del password
		email = self.cleaned_data.get('email');
		password = self.cleaned_data.get('password');

		#autenticar el usuario, de que exista el user
		#authenticate devuelve true o false
		#si todo esta bien todo queda guardao den user_cache
		self.user_cache = authenticate(email=email, password=password);

		if self.user_cache is None:
			raise forms.ValidationError('Usuario incorrecto');
		elif not self.user_cache.is_active:
			raise forms.ValidationError('Usuario inactivo');

		return self.cleaned_data 

		#devuelve el usuario
	def get_user(self):
		return self.user_cache;
