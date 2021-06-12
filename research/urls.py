from django.urls import path
from django.conf.urls import url

from .views import *

app_name = 'research'

urlpatterns = [
    path('', ResearchHomeDashboardView.as_view(), name='research_home'),
    path('program/', ResearchProgramListView.as_view(), name='programs')
]

urlpatterns += [
    url('program/create/$', ResearchProgramCreateView.as_view(), name='program_create'),
    url('program/(?P<pk>\d+)/update/$', ResearchProgramUpdateView.as_view(), name='program_update'),
]
