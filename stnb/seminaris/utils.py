# -*- coding: utf-8 -*-
import re

from django.utils.translation import ugettext as _

from stnb.membres.utils import cognoms_lexic

def persones_nom_cognoms(persones_str):
    if re.match(r'^\s*$', persones_str):
        return [ ]
    persones = [ ]
    for p in re.split(r'\s*,\s*', persones_str):
        div = re.split(r'\s+', p)
        if len(div) == 2: # Fàcil
            persones.append({'nom': div[0],
                             'cognoms': div[1],})
        else:
            persones.append({'nom': div[0],
                             'cognoms': ' '.join(div[1:])})
    
    return persones

def persona_html(p):
    html = ''
    if isinstance(p, dict):
        html = '%s %s' % (p['nom'], p['cognoms'])
    elif p.amagar_perfil:
        html = '%s %s' % (p.nom, p.cognoms)
    else:
        html = '<a href="%s">%s %s</a>' % (p.get_absolute_url(),
                                           p.nom, p.cognoms)

    return html

def persones_html(persones):
    if len(persones) == 0:
        return ''

    html = ''
    if len(persones) == 1:
        html = persona_html(persones[0])
    else:
        persones.sort(key=lambda p: cognoms_lexic(p))
        persones_html = [ persona_html(p) for p in persones ]
       
        html = '%s %s %s' % (', '.join(persones_html[0:-1]),
                             _('and'), persones_html[-1],)

    return html

