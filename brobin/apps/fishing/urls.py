from django.urls import path
from .views import FishingStatsView, FishingYearView


urlpatterns = [
    path('<int:year>/', FishingYearView.as_view()),
    path('', FishingStatsView.as_view()),
]
