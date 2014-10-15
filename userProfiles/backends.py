from django.contrib.auth.models import User

class EmailBackend(object):
	def authenticate(self, email=None, password=None):
		try:
			#trate de traerme un usuario con ese email
			user = User.objects.get(email=email);
			#si lo encuentra verifique su password
			#usamos ceckpassword por que tiene hash
			if user.check_password(password):
				return user; 
			#si el usuario o passwor incorrecto devuelve None
		except User.DoesNotExist:
			return None;

	def get_user(self, userId):
		try:
			#busque un usuario en que el id del usuario sea el user id que esta 
			#llegano a la funcion
			return User.objects.get(id=userId); #retorna el user
		except User.DoesNotExist:
			return 	None;