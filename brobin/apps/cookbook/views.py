from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Recipe
from .serializers import RecipeSerializer


class RecipeDetailView(RetrieveAPIView):
    serializer_class = RecipeSerializer
    model = Recipe

    def get_object(self, *args, **kwargs):
        return get_object_or_404(Recipe, slug=self.kwargs.get('slug'))


class RecipeListView(ListAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

