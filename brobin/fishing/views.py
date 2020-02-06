from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView

from .forms import FishForm
from .models import Year
from .utils import *


def index(request):
    bar = year_compare_bar()
    line = year_compare_line()
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


class AddFishView(CreateView):
    model = BigFish
    template_name = 'fishing/add.html'
    form_class = FishForm

    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated():
            return redirect('fishing-index')
        return super(AddFishView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        messages.info(self.request, '{0} added!'.format(str(self.object)))
        return reverse('fishing-add')
