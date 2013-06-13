# -*- coding: utf-8 -*-
import re
import os
from PIL import Image

from django.conf import settings

def cognoms_lexic(membre_o_dict):
    if isinstance(membre_o_dict, dict):
        cognoms = membre_o_dict['cognoms']
    else:
        cognoms = unicode(membre_o_dict.cognoms)

    regexp = r'^(((de|von|van|a)\s+)|a\')'
    cognoms = re.sub(regexp, '', cognoms)

    return cognoms.lower()

def comparar_cognoms(membre_o_dict_a, membre_o_dict_b):
    return cognoms_lexic(membre_o_dict_a) < cognoms_lexic(membre_o_dict_b)

def crear_imagen_petita(path_orig, path_dest, ample):
        file, ext = os.path.splitext(path_orig)
        im = Image.open(path_orig)
        alcada = im.size[1] * ample / im.size[0]
        im.thumbnail((ample, alcada), Image.ANTIALIAS)
        im.save(os.path.join(settings.MEDIA_ROOT, path_dest), "PNG")

