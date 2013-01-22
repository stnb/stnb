# -*- coding: utf-8 -*-
import re

from stnb.membres.utils import cognoms_lexic

def persones_nom_cognoms(persones_str):
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

def persones_html(persones):
    persones.sort(key=lambda p: cognoms_lexic(p))

    persones_html = [ ]
    for p in persones:
        if isinstance(p, dict):
            persones_html.append('%s %s' % (p['nom'], p['cognoms']))
        elif p.amagar_perfil:
            persones_html.append('%s %s' % (p.nom, p.cognoms))
        else:
            persones_html.append('<a href="%s">%s %s</a>' %
                    (p.get_absolute_url(), p.nom, p.cognoms))

    return ', '.join(persones_html)

