from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stnb.views.home', name='home'),
    # url(r'^stnb/', include('stnb.foo.urls')),
    url(r'^institucions/', include('stnb.institucions.urls')),
    #url(r'^seminaris/', include('stnb.seminaris.urls')),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
