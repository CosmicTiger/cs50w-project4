from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class AnimalsDashboardView(TemplateView):
    template_name = "primitiva_ecosystem/dashboard_animalia.html"

@method_decorator(login_required, name='dispatch')
class PlantsDashboardView(TemplateView):
    template_name = "primitiva_ecosystem/dashboard_plantae.html"

@method_decorator(login_required, name='dispatch')
class EcosystemsDashboardView(TemplateView):
    template_name = "primitiva_ecosystem/dashboard_ecosystem.html"
