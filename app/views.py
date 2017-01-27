from django.db.models import Sum
from django.views.generic import ListView

from app.models import Point


class TeamPointsList(ListView):
    model = Point
    template_name = 'team_list.html'
    queryset = Point.objects.values('user__team__name').order_by().\
        annotate(Sum('points'))


