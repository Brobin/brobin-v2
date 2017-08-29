import csv

from datetime import timedelta

from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
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


def get_chart(**kwargs):
    labels, mystic, valor, instinct = [], [], [], []
    for log in GymLog.objects.filter(**kwargs).order_by('created'):
        labels.append(log.created)
        mystic.append(log.mystic)
        valor.append(log.valor)
        instinct.append(log.instinct)
    chart = pygal.Line(style=style, stroke_style={'width': 5},
                       width=1200, show_x_labels=False)
    chart.x_labels = map(lambda d: localtime(d).strftime('%m-%d %I:%M %p'), labels)
    chart.add("Mystic", mystic)
    chart.add("Valor", valor)
    chart.add("Instinct", instinct)
    return chart


def gyms_graph(request):
    all_time = get_chart(**{})
    last_day = get_chart(**{'created__gte': timezone.now() - timedelta(days=1)})
    last_three = get_chart(**{'created__gte': timezone.now() - timedelta(days=3)})
    last_week = get_chart(**{'created__gte': timezone.now() - timedelta(days=7)})

    mystic = GymLog.objects.aggregate(avg=Avg('mystic'))['avg']
    valor = GymLog.objects.aggregate(avg=Avg('valor'))['avg']
    instinct = GymLog.objects.aggregate(avg=Avg('instinct'))['avg']
    total = mystic + valor + instinct

    context = {
        'all_time': all_time.render(is_unicode=True),
        'last_day': last_day.render(is_unicode=True),
        'last_three': last_three.render(is_unicode=True),
        'last_week': last_week.render(is_unicode=True),
        'recent': GymLog.objects.order_by('-created')[:12],
        'mystic_pct': mystic / total * 100,
        'valor_pct': valor / total * 100,
        'instinct_pct': instinct / total * 100,
    }
    return render(request, 'gyms/gyms.html', context)
