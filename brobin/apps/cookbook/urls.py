from django.urls import path
from .views import(
    RecipeDetailView,
    RecipeListView,
)


urlpatterns = [
    path('<str:slug>', RecipeDetailView.as_view()),
    path('', RecipeListView.as_view()),
]
