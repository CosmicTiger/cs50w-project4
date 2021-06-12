from django.urls import path

from .views import StaffDashboardView

app_name = 'staff'

urlpatterns = [
    path('staff/', StaffDashboardView.as_view(), name='staff_home'),
]
