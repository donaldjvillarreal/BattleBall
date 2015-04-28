''' master url file, for battleball's urls, go to the urls.py under battleball '''
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^battleball/', include('battleball.urls')),
                      )

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
                            (r'^media/(?P<path>.*)',
                             'serve',
                             {'document_root': settings.MEDIA_ROOT}), )
