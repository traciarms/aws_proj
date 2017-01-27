from __future__ import unicode_literals

from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=250)
    date_created = models.DateField(auto_created=True)
    date_updated = models.DateField(auto_now_add=True)


class User(models.Model):
    name = models.CharField(max_length=250)
    team = models.ForeignKey(Team, null=True)
    date_created = models.DateField(auto_created=True)
    date_updated = models.DateField(auto_now_add=True)


class Points(models.Model):
    user = models.ForeignKey(User, null=True)
    points = models.IntegerField()
    reason = models.CharField(max_length=250)
    date_created = models.DateField(auto_created=True)

