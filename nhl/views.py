import requests

from django.http import Http404
from django.views.generic import TemplateView

from .enums import TEAMS


ROSTER_URL = 'https://statsapi.web.nhl.com/api/v1/teams?teamId={0}&expand=team.roster,roster.person,person.stats&stats=statsSingleSeason'  # NOQA


class NHLView(TemplateView):
    template_name = 'nhl/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(NHLView, self).get_context_data(*args, **kwargs)
        context['teams'] = [key for key, id in TEAMS.items()]
        context['teams'].sort()
        return context


class NHLTeamView(TemplateView):
    template_name = 'nhl/team.html'

    def dispatch(self, *args, **kwargs):
        self.team = self.kwargs.get('team').upper()
        if self.team not in TEAMS:
            return Http404()
        return super(NHLTeamView, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(NHLTeamView, self).get_context_data(*args, **kwargs)
        self.team_id = TEAMS[self.team]
        self.get_roster()
        context['skaters'] = self.skaters
        context['goalies'] = self.goalies
        context['team'] = self.team
        return context

    def get_roster(self):
        url = ROSTER_URL.format(self.team_id)
        data = requests.get(url).json()['teams'][0]['roster']
        self.skaters = []
        self.goalies = []
        for player in data['roster']:
            if player['person']['primaryPosition']['abbreviation'] == 'G':
                self.goalies.append(player)
            else:
                self.skaters.append(player)
        self.skaters.sort(
            key=lambda x: x['person']['stats'][0]['splits'][0]['stat']['points'],
            reverse=True
        )
