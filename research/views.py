from django.views.generic.base import TemplateView
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView,
    UpdateView
)
from .models import *
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


@method_decorator(login_required, name='dispatch')
class ResearchHomeDashboardView(TemplateView):
    template_name = "research/research_index.html"

@method_decorator(login_required, name='dispatch')
class ResearchProgramListView(ListView):
    model = Program
    success_url = reverse_lazy('research:research_home')

@method_decorator(login_required, name='dispatch')
class ResearchProgramCreateView(LoginRequiredMixin, CreateView):
    model = Program
    success_url = reverse_lazy('research:programs_list')

@method_decorator(login_required, name='dispatch')
class ResearchProgramUpdateView(LoginRequiredMixin, UpdateView):
    model = Program
    fields = '__all__'
    success_url = reverse_lazy('dashboard_home')
