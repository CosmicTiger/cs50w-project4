from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class StaffDashboardView(TemplateView):
    template_name = "research/dashboard.html"
