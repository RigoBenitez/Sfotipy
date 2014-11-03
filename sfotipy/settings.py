"""
Django settings for sfotipy project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rv6nc3wwo-q$_*^+xb&j#i76@34-^bdoe%pn=6pe_o-pqx2xp3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

#Para filter de API rest
#Filtrar para los elementos del modelo
REST_FRAMEWORK ={
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)    
}

#para que sirva DEBUG = False
ALLOWED_HOSTS = ['localhost']


#un archivo que por defecto debe de llamarse context_procesors
TEMPLATE_CONTEXT_PROCESSORS = TCP + ( "django.core.context_processors.request", 'sfotipy.context_processors.basico', )

GRAPPELLI_ADMIN_TITLE = 'Sfoti.py' 

# Application definition

INSTALLED_APPS = (
   'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'mockups',
    'django_extensions',
    'rest_framework',
    'redis_cache',
    'sorl.thumbnail',
    'userProfiles',
    'artists',
    'albums',
    'tracks',
)

MIDDLEWARE_CLASSES = (
    # para cache de middleware es el primero que debe de ir
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #siempre tiene que ser el ultimo
    'django.middleware.cache.FetchFromCacheMiddleware',
    # 'sfotipy.middleware.PaisMiddleware',
)

ROOT_URLCONF = 'sfotipy.urls'

WSGI_APPLICATION = 'sfotipy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sfotipy',
        'USER': 'root',
        'PASSWORD': 'Angel1991',
        # 'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.RedisCache',
#         'LOCATION': 'localhost: 6379',
#         'OPTIONS': {
#             'DB': 1,
#             #opcional pero lo hace mas rapido en produccion
#             'PARSER_CLASS': 'redis.connection.HiredisParser',
#         }
    
# }}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder')

#
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

MEDIA_ROOT =  os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['media'])
#usar collectstatic en el mange.py para que no se tenga que hacer el f5

STATIC_ROOT =  os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['content'])

MEDIA_URL = '/media/'

#backends
AUTHENTICATION_BACKENDS = ('userProfiles.backends.EmailBackend',);



#----------------------------caches------------------------------------
#para no darle TAN duro a la db
#crea el elemento en la db (lento), pero cada que el usuario visite mas paginas saca todo de la cache 
#SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

#aun mas -- si no les importa que se pierda la sesion
#no usa una base de datos para guardar el cache
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

#a los usuarios no logeados
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
#----------------------------caches------------------------------------

