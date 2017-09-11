import csv
import os
from django.core.management.base import BaseCommand

from gyms.models import GymLog


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        """Get the filepath and process the csv"""
        filepath = os.path.join('./', options['csv_file'])
        with open(filepath) as _file:
            reader = csv.reader(_file, delimiter=',')
            for row in reader:
                GymLog.objects.create(
                    created=row[0],
                    mystic=row[1],
                    valor=row[2],
                    instinct=row[3],
                )
