from django.urls import path
from . import views

urlpatterns = [
    path('', views.daily_summary, name='daily_summary'),
]
