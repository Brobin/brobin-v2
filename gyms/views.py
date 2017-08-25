import csv

from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import localtime

import pygal

from .models import GymLog


style = pygal.style.Style(
    colors=('#3366cc', '#dc3912', '#ff9900')
)


def lincoln_gyms(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="gyms.csv"'
    logs = GymLog.objects.order_by('created')
    writer = csv.writer(response)
    for log in logs:
        writer.writerow([log.created, log.mystic, log.valor, log.instinct])
    return response

def gyms_graph(request):
    labels, mystic, valor, instinct = [], [], [], []
    for log in GymLog.objects.order_by('created'):
        labels.append(log.created)
        mystic.append(log.mystic)
        valor.append(log.valor)
        instinct.append(log.instinct)
    chart = pygal.Line(style=style, stroke_style={'width': 5}, width=1200, show_x_labels=False)
    chart.x_labels = map(lambda d: localtime(d).strftime('%m-%d %I:%M %p'), labels)
    chart.add("Mystic", mystic)
    chart.add("Valor", valor)
    chart.add("Instinct", instinct)
    context = {
        'chart': chart.render(is_unicode=True),
        'recent': GymLog.objects.order_by('-created')[:12],
        'mystic_avg': GymLog.objects.aggregate(avg=Avg('mystic'))['avg'],
        'valor_avg': GymLog.objects.aggregate(avg=Avg('valor'))['avg'],
        'instinct_avg': GymLog.objects.aggregate(avg=Avg('instinct'))['avg'],
    }
    return render(request, 'gyms/gyms.html', context)
