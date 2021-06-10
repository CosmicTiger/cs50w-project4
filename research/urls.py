from django.urls import path

from .views import ResearchHomeDashboardView

urlpatterns = [
    path('', ResearchHomeDashboardView.as_view(), name='research_home'),
]
