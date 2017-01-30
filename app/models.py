from __future__ import unicode_literals

from django.db import models
from datetime import datetime


class Team(models.Model):
    """ The team model, contains name and date information """
    name = models.CharField(max_length=250)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    date_updated = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return ("Name: {}, date created: {}, date updated: {}"
                .format(self.name, self.date_created, self.date_updated))


class AUser(models.Model):
    """ The User model, user name and the team they belong to """
    name = models.CharField(max_length=250)
    team = models.ForeignKey(Team, null=True)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    date_updated = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return ("Name: {}, team: {}, date created: {}, date updated: {}"
                .format(self.name, self.team.name, self.date_created,
                        self.date_updated))


class Point(models.Model):
    """ Point model, links to the User and contains the reason for the
    points as well as the date the points were created """
    user = models.ForeignKey(AUser, null=True)
    points = models.IntegerField()
    reason = models.CharField(max_length=250)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return ("User: {}, points: {}, reason: {}, date created: {}"
                .format(self.user.name, self.points, self.reason,
                        self.date_created))

