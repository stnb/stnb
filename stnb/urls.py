from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stnb.views.home', name='home'),
    # url(r'^stnb/', include('stnb.foo.urls')),
    #url(r'^seminaris/', include('stnb.seminaris.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^setlang/', 'stnb.i18n.views.set_language', name='set-language'),
    (r'^i18n/', include('django.conf.urls.i18n')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += i18n_patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='inici'),
    

    url(r'^sobre-stnb/$', TemplateView.as_view(template_name='sobre-stnb/sobre-stnb.html'), name='sobre-stnb'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    
    url(r'^comptes/', include('stnb.comptes.urls')),
    url(r'^institucions/', include('stnb.institucions.urls')),
    url(r'^seminaris/', include('stnb.seminaris.urls')),
)

