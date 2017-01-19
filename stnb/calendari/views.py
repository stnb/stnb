# -*- coding: utf-8 -*-
import datetime

from django.views.generic import TemplateView

from stnb.seminaris.models import Seminari
from stnb.esdeveniments.models import Esdeveniment

class CalendariListView(TemplateView):
    template_name = 'calendari/llista.html'

    def get_context_data(self, **kwargs):
        context = super(CalendariListView, self).get_context_data(**kwargs)

        seminaris = Seminari.objects.filter(data_finalizacio__gte=datetime.datetime.now)
        esdeveniments = Esdeveniment.objects.filter(data__gte=datetime.datetime.now)

        items = [ { 'seminari': s } for s in list(seminaris) ] + \
                [ { 'esdeveniment': e } for e in list(esdeveniments) ]

        def item_data(item):
            if 'seminari' in item:
                return item['seminari'].data_inici
            elif 'esdeveniment' in item:
                return item['esdeveniment'].data
            else:
                return datetime.datetime(year=1970, month=1, day=1)

        def cmp_item_data(a, b):
            return cmp(item_data(a), item_data(b))

        items.sort(cmp_item_data)

        context.update({ 'items': items })

        return context

