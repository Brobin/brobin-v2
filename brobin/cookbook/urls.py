from django.urls import path
from .views import(
    RecipeList,
    RecipeDetail,
)


urlpatterns = [
    path('<slug>/', RecipeDetail.as_view(), name='recipe'),
    path('', RecipeList.as_view(), name='cookbook'),
]
