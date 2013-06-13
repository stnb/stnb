import datetime
import logging
from optparse import make_option

from django.core.management.base import BaseCommand

from stnb.membres.models import Membre

class Command(BaseCommand):
    """
    Re-creates all the resized images for all the Membre objects.
    """
    option_list = BaseCommand.option_list
    args = ''
    requires_model_validation = False

    def handle(self, **options):
        logging.basicConfig(level={'0':logging.ERROR, '1':logging.WARNING,
                                   '2':logging.INFO, '3':logging.DEBUG,}\
                                           [options['verbosity']],
                            format="%(message)s")

    
        membres = Membre.objects.filter(foto__isnull=False)
        logging.info('Processing photos for {0} members.'.format(len(membres)))
        for membre in membres:
            if membre.foto:
                membre.crear_totes_fotos()


