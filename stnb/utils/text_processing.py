import unicodedata

def text_sense_accents(text):
    nfd_text = ''.join((c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn'))
    return nfd_text

