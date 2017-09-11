from django.contrib import admin

from .models import GymLog

@admin.register(GymLog)
class GymLogAdmin(admin.ModelAdmin):
    list_display = ['created', 'mystic', 'valor', 'instinct']
