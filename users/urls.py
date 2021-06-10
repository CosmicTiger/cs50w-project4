from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('sign-in/', views.sign_in, name='sign-in')
]
