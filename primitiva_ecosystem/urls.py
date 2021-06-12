from django.urls import path

from .views import *

app_name = 'ecosystems'

urlpatterns = [
    path('', TemplateView.as_view(template_name="primitiva_ecosystems/dashboard_ecosystem.html"), name="natura"),
    path('animalia/', AnimalsDashboardView.as_view(), name='animalia_home'),
    path('plants/', PlantsDashboardView.as_view(), name='plantae_home'),
    path('ecosystems/', EcosystemsDashboardView.as_view(), name='ecosystems_home'),
]
