from datetime import datetime

import requests

from django.http import Http404
from django.views.generic import TemplateView

from .enums import TEAMS


STANDINGS_URL = 'http://statsapi.web.nhl.com/api/v1/standings?expand=standings.record,standings.team,standings.division,standings.conference,team.stats'  # NOQA
ROSTER_URL = 'https://statsapi.web.nhl.com/api/v1/teams?teamId={0}&expand=team.roster,roster.person,person.stats&stats=statsSingleSeason'  # NOQA
GAMES_URL = 'http://www.nhl.com/stats/rest/team?isAggregate=false&reportType=basic&isGame=true&reportName=teamsummary&cayenneExp=gameDate>="{0}" and gameDate<="{1}" and gameTypeId={2} and teamId={3}&sort=gameId'  # NOQA


class NHLView(TemplateView):
    template_name = 'nhl/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(NHLView, self).get_context_data(*args, **kwargs)
        data = requests.get(STANDINGS_URL).json()['records']
        context['divisions'] = data
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
        context['chart'] = self.get_points_chart()
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
        self.skaters = [
            s for s in self.skaters
            if len(s['person']['stats'][0]['splits']) > 0
        ]
        self.skaters.sort(
            key=lambda x: x['person']['stats'][0]['splits'][0]['stat']['points'],
            reverse=True
        )

    def get_points_chart(self):
        format = '%Y-%m-%dT%H:%M:%S.000Z'
        url = GAMES_URL.format(
            datetime(2017, 10, 4).strftime(format),
            datetime.now().strftime(format),
            2, self.team_id
        )
        points, points_possible, = 0, 0
        goals, points_pct, labels = [], [], []
        for game in requests.get(url).json()['data']:
            points += game['wins'] * 2 + game['otLosses']
            points_possible += 2
            label = '{0} vs. {1}'.format(game['gameDate'][:10], game['opponentTeamAbbrev'])
            points_pct.append({
                'value': points / points_possible,
                'meta': label,
            })
            goals.append({
                'value': game['goalsFor'] - game['goalsAgainst'],
                'meta': label,
            })
            labels.append(points_possible / 2)
        return {
            'points_pct': points_pct[10:],
            'points_pct_labels': labels[10:],
            'goals': goals,
            'goals_labels': labels
        }
