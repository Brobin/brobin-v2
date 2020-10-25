from django.contrib import admin

from .models import Recipe, Ingredient, IngredientAmount, Step


class IngredientInline(admin.TabularInline):
    model = IngredientAmount
    extra = 1
    fields = ['amount', 'ingredient', 'order']
    raw_id_fields = ['ingredient']
    ordering = ['order']


class StepInline(admin.StackedInline):
    model = Step
    extra = 1


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'notes']
    list_display_links = ['title']
    inlines = [IngredientInline, StepInline]
