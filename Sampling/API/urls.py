from django.urls import path
from . import views

urlpatterns = [
    path('stratified/', views.stratified_sampling, name='stratified_sampling'),
    path('systematic/', views.systematic_sampling,name='systematic_sampling'),
    path('simple_random/', views.simple_random_sampling,name='simple_random_sampling'),
    path('cluster_sampling/', views.cluster_sampling,name='cluster_sampling'),
    path('purposive_sampling/', views.purposive_sampling,name='purposive_sampling'),
    
    
]