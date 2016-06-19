from django.shortcuts import render

import pygal
from pygal.style import BlueStyle

from .models import Year


def index(request):
    return render(request, "index.html")


def year(request, year):
    year = Year.objects.get(year=year)
    chart = pygal.XY(stroke=False, style=BlueStyle)
    chart.x_label = ["Weight (pounds)"]
    chart.y_label = ["Length (inches)"]
    chart.add("Bass", [(n.weight, n.length) for n in year.big_bass])
    chart.add("Northern", [(n.weight, n.length) for n in year.big_northern])
    chart.add("Walleye", [(n.weight, n.length) for n in year.big_walleye])
    chart.title = "Biggest Fish"
    chart = chart.render(is_unicode=True)
    punchcard = _daily_punchcard(year)
    data = {"year": year, "chart": chart, "punchcard": punchcard}
    return render(request, "year.html", data)


def _daily_punchcard(year):
    chart = pygal.Dot(style=BlueStyle)
    chart.title = "Frequency of Fish"
    chart.x_labels = ["Saturday", "Sunday", "Monday", "Tuesday",
                      "Wednesday", "Thursday", "Friday"]
    bass, crappie, northern, walleye = [], [], [], []
    for day in year.days.order_by("day"):
        bass.append(day.bass)
        crappie.append(day.crappie)
        northern.append(day.northern)
        walleye.append(day.walleye)
    chart.add("Bass", bass)
    chart.add("Crappie", crappie)
    chart.add("Northern", northern)
    chart.add("Walleye", walleye)
    return chart.render(is_unicode=True)
