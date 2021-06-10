from django.urls import path
from . import views

app_name = 'primitiva_staff'

urlpatterns = [
    path('', views.index, name='staff_home')
]
