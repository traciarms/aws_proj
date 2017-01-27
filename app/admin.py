from django.contrib import admin

from app.models import Team, Point, AUser


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created', 'date_updated')


class AUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'date_created', 'date_updated')


class PointsAdmin(admin.ModelAdmin):
    list_display = ('user', 'points', 'reason', 'date_created')


admin.site.register(Team, TeamAdmin)
admin.site.register(AUser, AUserAdmin)
admin.site.register(Point, PointsAdmin)
