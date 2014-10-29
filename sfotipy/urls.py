from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

#para class base view
from artists.views import ArtistDetailView

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


)

urlpatterns += patterns('', 
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,} ),
)
