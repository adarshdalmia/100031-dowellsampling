from django.urls import path
from . import views

urlpatterns = [
    path('sample-size/<str:population>/', views.calculate_sample_size),
]
