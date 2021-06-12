from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.urls import path, include
from . import views

urlpatterns = [
    # path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', views.RegisterView, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
