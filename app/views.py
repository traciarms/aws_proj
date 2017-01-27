from django.db.models import Sum
from django.views.generic import ListView

from app.models import Point


class TeamPointsList(ListView):
    """ View to list the teams and their scores """
    model = Point
    template_name = 'team_list.html'
    queryset = Point.objects.values('user__team__name').order_by().\
        annotate(Sum('points'))


