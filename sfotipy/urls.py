from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

#para class base view y para la API
from artists.views import ArtistDetailView, ArtistViewSet
from albums.views import AlbumViewSet
from tracks.views import TrackViewSet
#son los que le permiten enlazar a los diferentes recursos de la API
from rest_framework import routers

router = routers.DefaultRouter();
router.register(r'artists', ArtistViewSet);
router.register(r'albums', AlbumViewSet);
router.register(r'tracks', TrackViewSet);

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sfotipy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tracks/(?P<title>[\w\-\s]+)', 'tracks.views.trackView', name='trackView'),
    url(r'^signup/', 'userProfiles.views.signup', name='signup'),
    url(r'^signin/', 'userProfiles.views.signin', name='signin'),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    (r'^admin/',  include(admin.site.urls)), # admin site
    #para la class base view CBV
    #pk es la primary key (id)->atributo que se le pasa a la lista
    #Se invoca a la clase y se le pone .as_view()
    url(r'^artists/(?P<pk>[\d]+)', ArtistDetailView.as_view(),), 
    #incluir todas las urls del router
    url(r'^api/', include(router.urls)), 

    #autenticar API
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), 


)

urlpatterns += patterns('', 
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,} ),
)
