# -*- coding: utf-8 -*-
import re

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

