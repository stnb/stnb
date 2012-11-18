from django.views.generic import ListView, DetailView

from .models import Institucio

class InstitucioListView(ListView):
    model = Institucio
    context_object_name = 'institucions'
    template_name = 'institucions/institucio_llista.html'

    queryset = Institucio.objects.all()

class InstitucioDetailView(DetailView):
    model = Institucio
    context_object_name = 'institucio'
    template_name = 'institucions/institucio_detall.html'

    queryset = Institucio.objects.all()
    slug_field = 'nom_curt'

