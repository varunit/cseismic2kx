from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^cseismic2kx/', include('cseismic2kx.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^$', 'home.views.index'),
    url(r'^activate/(?P<activation_key>\w+)/$', 'registration.views.activate', { 'backend': 'registration.backends.default.DefaultBackend' }, name='registration_activate'),
    url(r'^account/signup/$', 'registration.views.register', {'backend':'registration.backends.default.DefaultBackend' }, name='registration_register'),
    (r'^account/', include('django_authopenid.urls')),
)
