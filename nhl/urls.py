from django.conf.urls import url

from .views import NHLView, NHLTeamView


urlpatterns = [
    url(r'^(?P<team>.*)/$', NHLTeamView.as_view(), name='nhl-team'),
    url(r'^$', NHLView.as_view(), name='nhl'),
]
