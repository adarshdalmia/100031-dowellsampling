from django.urls import path
from . import views

urlpatterns = [
    path('stratified/', views.stratified_sampling, name='stratified_sampling'),
    path('systematic/', views.systematic_sampling, name='systematic_sampling'),
    path('simple_random/', views.simple_random_sampling, name='simple_random_sampling'),
    # path('', views.sampling_input, name='sampling_input'),
    path('cluster_sampling/', views.cluster_sampling, name='cluster_sampling'),
    path('purposive_sampling/', views.purposive_sampling, name='purposive_sampling'),
    # path('stratified_sampling_input/', views.stratified_sampling_input,name='stratified_sampling_input'),
    # path('systematic_sampling_input/', views.systematic_sampling_input,name='systematic_sampling_input'),
    # path('simple_random_sampling_input/', views.simple_random_sampling_input,name='simple_random_sampling_input'),
    # path('cluster_sampling_input/', views.cluster_sampling_input,name='cluster_sampling_input'),
    # path('purposive_sampling_input/', views.purposive_sampling_input,name='purposive_sampling_input'),
    # path('search-function/',views.search,name='search_function'),
    # path('dowell-search/',views.dowell_search,name='search_function_input'),

]
