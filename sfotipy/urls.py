from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sfotipy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tracks/(?P<title>[\w\-\s]+)', 'tracks.views.trackView', name='trackView'),
    url(r'^signup/', 'userProfiles.views.signup', name='signup'),
    url(r'^signin/', 'userProfiles.views.signin', name='signin'),
)
