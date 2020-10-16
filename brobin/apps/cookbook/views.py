from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Recipe


class RecipeList(ListView):
    template_name = 'recipe/list.html'
    model = Recipe


class RecipeDetail(DetailView):
    template_name = 'recipe/detail.html'
    model = Recipe

    def get_object(self, *args, **kwargs):
        return get_object_or_404(Recipe, slug=self.kwargs.get('slug'))