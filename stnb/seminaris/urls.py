from django.conf.urls.defaults import patterns, url

from .models import Seminari

urlpatterns = patterns('',
    url(r'(?P<slug>[a-z0-9\-]+)/$',
        'django.views.generic.list_detail.object_detail',
        { 'queryset': Seminari.objects.all(), 'slug_field': 'slug' },
        name='seminari-detall'),
)
