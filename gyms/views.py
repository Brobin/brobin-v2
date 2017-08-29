import csv

from datetime import timedelta

from django.db.models import Avg, Max, Min
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
    data = GymLog.objects.filter(**kwargs).aggregate(
        mystic_avg=Avg('mystic'),
        mystic_min=Min('mystic'),
        mystic_max=Max('mystic'),
        valor_avg=Avg('valor'),
        valor_min=Min('valor'),
        valor_max=Max('valor'),
        instinct_avg=Avg('instinct'),
        instinct_min=Min('instinct'),
        instinct_max=Max('instinct'),
    )
    total = data['mystic_avg'] + data['valor_avg'] + data['instinct_avg']
    return chart, data, total


def gyms_graph(request):
    all_time, at_data, at_total = get_chart(**{})
    last_day, ld_data, ld_total = get_chart(
        **{'created__gte': timezone.now() - timedelta(days=1)})
    last_three, lt_data, lt_total = get_chart(
        **{'created__gte': timezone.now() - timedelta(days=3)})
    last_week, lw_data, lw_total = get_chart(
        **{'created__gte': timezone.now() - timedelta(days=7)})

    context = {
        'all_time': {
            'chart': all_time.render(is_unicode=True),
            'data': at_data,
            'mystic': at_data['mystic_avg'] / at_total * 100,
            'valor': at_data['valor_avg'] / at_total * 100,
            'instinct': at_data['instinct_avg'] / at_total * 100,
        },
        'last_day': {
            'chart': last_day.render(is_unicode=True),
            'data': ld_data,
            'mystic': ld_data['mystic_avg'] / ld_total * 100,
            'valor': ld_data['valor_avg'] / ld_total * 100,
            'instinct': ld_data['instinct_avg'] / ld_total * 100,
        },
        'last_three': {
            'chart': last_three.render(is_unicode=True),
            'data': lt_data,
            'mystic': lt_data['mystic_avg'] / lt_total * 100,
            'valor': lt_data['valor_avg'] / lt_total * 100,
            'instinct': lt_data['instinct_avg'] / lt_total * 100,
        },
        'last_week': {
            'chart': last_week.render(is_unicode=True),
            'data': lw_data,
            'mystic': lw_data['mystic_avg'] / lw_total * 100,
            'valor': lw_data['valor_avg'] / lw_total * 100,
            'instinct': lw_data['instinct_avg'] / lw_total * 100,
        },
        'recent': GymLog.objects.order_by('-created')[:12],
    }
    return render(request, 'gyms/gyms.html', context)
