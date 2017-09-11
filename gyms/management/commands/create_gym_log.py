import requests

from collections import Counter

from django.core.management.base import BaseCommand
from django.utils import timezone

from gyms.models import GymLog


class Command(BaseCommand):

    def handle(self, *args, **options):
        url = 'http://lincroad.com/raw_data?pokemon=false&pokestops=false&luredonly=false&gyms=true&scanned=false&spawnpoints=false'  # NOQA
        data = requests.get(url)
        gyms = data.json()['gyms']
        teams = [gyms[key]['team_id'] for key in gyms]

        counter = dict(Counter(teams))
        
        GymLog.objects.create(
            created=timezone.now(),
            mystic=counter[1],
            valor=counter[2],
            instinct=counter[3],
        )
