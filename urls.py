from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'btc.views.home', name='home'),
    # url(r'^btc/', include('btc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('zinnia.urls')),
	url(r'^comments/', include('django.contrib.comments.urls')),
	url(r'^tinymce/', include('tinymce.urls')),
    #url(r'^admin/filebrowser/', include('filebrowser.urls')),
    #url(r'^grappelli/', include('grappelli.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,'show_indexes': True}),
)
urlpatterns += staticfiles_urlpatterns()