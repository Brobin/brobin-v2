import pygal
from pygal.style import DarkSolarizedStyle

from .models import Day, Year


def _year_compare_data():
    result = []
    for year in Year.objects.all():
        data = []
        for day in year.days.order_by("day"):
            data.append(day.total)
        result.append((str(year), data))
    return result


def year_compare_bar():
    chart = pygal.Bar(style=DarkSolarizedStyle)
    chart.x_labels = [x[0] for x in Day.DAYS]
    for year, datum in _year_compare_data():
        chart.add(year, datum)
    return chart.render(is_unicode=True)


def year_compare_punchcard():
    chart = pygal.Dot(style=DarkSolarizedStyle)
    chart.x_labels = [x[0] for x in Day.DAYS]
    for year, datum in _year_compare_data():
        chart.add(year, datum)
    return chart.render(is_unicode=True)


def daily_species_chart(year, chart_type="Dot"):
    chart = {
        "Dot": pygal.Dot,
        "Pie": pygal.Pie,
        "StackedBar": pygal.StackedBar,
    }[chart_type](style=DarkSolarizedStyle)
    chart.x_labels = [x[0] for x in Day.DAYS]
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


def year_size_scatter(year):
    chart = pygal.XY(stroke=False, style=DarkSolarizedStyle)
    chart.x_label = ["Weight (pounds)"]
    chart.y_label = ["Length (inches)"]
    chart.add("Bass", year.bass)
    chart.add("Northern", year.northern)
    chart.add("Walleye", year.walleye)
    return chart.render(is_unicode=True)
