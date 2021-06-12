"""primitiva_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import DashboardHomeView, DashboardView
from .settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('', include('blog.urls', namespace='blog'), name="blog"),
    path('dashboard/home', DashboardHomeView.as_view(), name="dashboard_home"),
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
    # path('dashboard/', DashboardRedirectView.as_view(url="/account/login"), name=""),
    path('dashboard/research/', include('research.urls', namespace='dashboard'), name="research"),
    path('dashboard/natura/', include('primitiva_ecosystem.urls', namespace='ecosystems'), name="ecosystems"),
    path('dashboard/staff/', include('primitiva_staff.urls', namespace='staff'), name="staff"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('auth/', include('users.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT) + static(MEDIA_URL, document_root = MEDIA_ROOT)
