from django.conf.urls import url
from .views import (
    index,
    year,
    AddFishView
)


urlpatterns = [
    url(r'^(?P<year>[0-9]{4})$', year, name='fishing-year'),
    url(r'^add$', AddFishView.as_view(), name='fishing-add'),
    url(r'^$', index, name='fishing-index'),
]
