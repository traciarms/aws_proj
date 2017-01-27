from __future__ import unicode_literals

from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=250)
    date_created = models.DateField(auto_created=True)
    date_updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return ("Name: {}, date created: {}, date updated: {}"
                .format(self.name, self.date_created, self.date_updated))


class AUser(models.Model):
    name = models.CharField(max_length=250)
    team = models.ForeignKey(Team, null=True)
    date_created = models.DateField(auto_created=True)
    date_updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return ("Name: {}, team: {}, date created: {}, date updated: {}"
                .format(self.name, self.team.name, self.date_created,
                        self.date_updated))


class Point(models.Model):
    user = models.ForeignKey(AUser, null=True)
    points = models.IntegerField()
    reason = models.CharField(max_length=250)
    date_created = models.DateField(auto_created=True)

    def __str__(self):
        return ("User: {}, points: {}, reason: {}, date created: {}"
                .format(self.user.name, self.points, self.reason,
                        self.date_created))

