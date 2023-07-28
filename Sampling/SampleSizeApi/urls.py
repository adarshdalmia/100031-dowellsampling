from django.urls import path
from . import views

urlpatterns = [
    path('', views.sample_size),
    path('<str:api_key>/', views.sample_size_api),
]
