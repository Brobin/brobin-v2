from django.urls import path
from .views import (
    index,
    year,
    AddFishView
)


urlpatterns = [
    path('<int:year>/', year, name='fishing-year'),
    path('add/', AddFishView.as_view(), name='fishing-add'),
    path('', index, name='fishing-index'),
]
