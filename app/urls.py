from django.conf.urls import url

from app.views import TeamPointsList

urlpatterns = [

    url(r'', TeamPointsList.as_view(), name='team_list'),
]