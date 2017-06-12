from django.conf.urls import url
from fishing import views


urlpatterns = [
    url(r'^(?P<year>[0-9]{4})$', views.year, name='fishing-year'),
    url(r'^add$', views.AddFishView.as_view(), name='fishing-add'),
    url(r'^$', views.index, name='fishing-index'),
]
