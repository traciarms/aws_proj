from django.db.models import Sum
from django.test import TestCase
from django.urls import reverse

from app.models import Team, AUser, Point


class TeamScoreTests(TestCase):

    def test_team_score_equals(self):
        blue = Team.objects.create(name='blue')
        yellow = Team.objects.create(name='yellow')
        b_user = AUser.objects.create(name='user_1', team=blue)
        bb_user = AUser.objects.create(name='user_11', team=blue)
        y_user = AUser.objects.create(name='user_2', team=yellow)
        yy_user = AUser.objects.create(name='user_22', team=yellow)
        b_points = Point.objects.create(user=b_user, points=15, reason='win')
        bb_points = Point.objects.create(user=bb_user, points=25, reason='win')
        y_points = Point.objects.create(user=y_user, points=20, reason='win')
        yy_points = Point.objects.create(user=yy_user, points=5, reason='tie')

        points = Point.objects.values('user__team__name').annotate(Sum('points'))
        
	for point in points:
		
		if point['user__team__name'] == 'yellow':
			yellow_points = point['points__sum']
		if point['user__team__name'] == 'blue':
			blue_points = point['points__sum']	
	
        self.assertEqual(blue_points, b_points.points+bb_points.points)
        self.assertEqual(yellow_points, y_points.points+yy_points.points)


class TeamPointsListTests(TestCase):
    def test_team_points_list(self):

        response = self.client.get(reverse('team_list'))
        self.assertEqual(response.status_code, 200, msg='found page')
