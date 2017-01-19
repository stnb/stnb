from django import template
from django.utils.translation import ugettext_lazy as _
register = template.Library()

def is_owner(user, obj):
    if user.is_authenticated() is False or 'is_owned_by' not in dir(obj):
        return False

    if user.is_staff or obj.is_owned_by(user):
        return True
    else:
        return False

def duracio(seminari):
    dstr = ''
    if seminari.data_inici.year == seminari.data_finalizacio.year:
        if seminari.data_inici.month == seminari.data_finalizacio.month:
            dstr= _('%(idia)s %(idata)d to %(fdia)s %(fdata)d %(imes)s, %(iany)d')
        else:
            dstr= _('%(idia)s %(idata)d %(imes)s to %(fdia)s %(fdata)d %(fmes)s, %(iany)d')
    else:
        dstr= _('%(idia)s %(idata)d %(imes)s, %(iany)d to %(fdia)s %(fdata)d %(fmes)s, %(fany)d')

    return dstr % { 'idia': _(seminari.data_inici.strftime('%A').decode('utf-8')),
                    'idata': seminari.data_inici.day,
                    'imes': _(seminari.data_inici.strftime('%B').decode('utf-8')),
                    'iany': seminari.data_inici.year,
                    'fdia': _(seminari.data_finalizacio.strftime('%A').decode('utf-8')),
                    'fdata': seminari.data_finalizacio.day,
                    'fmes': _(seminari.data_finalizacio.strftime('%B').decode('utf-8')),
                    'fany': seminari.data_finalizacio.year, }

register.filter('is_owner', is_owner)
register.filter('duracio', duracio)
