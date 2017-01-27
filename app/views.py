
from django.views.generic import ListView

from app.models import Team


class TeamPointsList(ListView):
    model = Team
    template_name = 'team_list.html'
    queryset = Team.objects.all().order_by('-auser__point__points')
