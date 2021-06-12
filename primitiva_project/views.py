from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from users.models import User

@method_decorator(login_required, name='dispatch')
class DashboardHomeView(TemplateView):
    template_name="research/dashboard_home.html"

@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'research/dashboard.html'
