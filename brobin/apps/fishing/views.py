from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Year
from .utils import *


class FishingStatsView(APIView):

    def get(self, request, *args, **kwargs):
        return Response({
            'bar': year_compare_bar(),
            'line': year_compare_line(),
            'punchcard': year_compare_punchcard(),
            'scatter': all_years_scatter(),
        })


class FishingYearView(APIView):

    def get(self, request, *args, **kwargs):
        year = get_object_or_404(Year, year=self.kwargs.get('year'))
        return Response({
            'pie': daily_species_chart(year, "Pie"),
            'bar': daily_species_chart(year, "StackedBar"),
            'punchcard': daily_species_chart(year, "Dot"),
            'scatter': year_size_scatter(year)
        })
