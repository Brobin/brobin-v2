import csv
from django.http import HttpResponse

from .models import GymLog


def lincoln_gyms(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="gyms.csv"'
    logs = GymLog.objects.order_by('created')
    writer = csv.writer(response)
    for log in logs:
        writer.writerow([log.created, log.mystic, log.valor, log.instinct])
    return response
