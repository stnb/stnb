from django.conf.urls.defaults import patterns, url

from .models import Institucio

urlpatterns = patterns('',
    url(r'(?P<slug>[a-z0-9\-]+)/$',
        'django.views.generic.list_detail.object_detail',
        { 'queryset': Institucio.objects.all(), 'slug_field': 'nom_curt' },
        name='institucio-llista'),
)
