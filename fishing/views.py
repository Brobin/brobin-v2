from django.shortcuts import render

from .models import Year
from .utils import *


def index(request):
    bar = year_compare_bar()
    punchcard = year_compare_punchcard()
    scatter = all_years_scatter()
    return render(request, "fishing/index.html", locals())


def year(request, year):
    year = Year.objects.get(year=year)
    pie = daily_species_chart(year, "Pie")
    bar = daily_species_chart(year, "StackedBar")
    punchcard = daily_species_chart(year, "Dot")
    scatter = year_size_scatter(year)
    return render(request, "fishing/year.html", locals())
