from django.views.generic.base import TemplateView
from django.shortcuts import render

class ResearchHomeDashboardView(TemplateView):
    template_name = "research/research_index.html"
