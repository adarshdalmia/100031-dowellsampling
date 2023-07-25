from django.urls import path
from . import views

urlpatterns = [
    path('sample-size/', views.calculate_sample_size),
]
