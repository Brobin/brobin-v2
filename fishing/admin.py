from django.contrib import admin

from .models import BigFish, Day, Year


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ['id', 'year']
    list_display_links = ['id', 'year']


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ['id', 'day', 'year', 'bass', 'crappie', 'northern', 'walleye']
    list_display_links = ['id', 'day']
    list_filter = ['day', 'year']


@admin.register(BigFish)
class BigFishAdmin(admin.ModelAdmin):
    list_display = ['id', 'year', 'species', 'length', 'weight']
    list_filter = ['year', 'species']
