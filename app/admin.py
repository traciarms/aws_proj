from django.contrib import admin

from app.models import Team, User, Points


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created', 'date_updated')


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'date_create', 'date_updated')


class PointsAdmin(admin.ModelAdmin):
    list_display = ('user', 'points', 'reason', 'date_created')


admin.site.register(Team, TeamAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Points, PointsAdmin)
