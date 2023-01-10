from django.urls import path
from . import views

urlpatterns = [
    path('stratified/', views.stratifiedSamplingAPI),
]