from django.urls import path
from . import views

app_name = "SamplingV2"

urlpatterns = [
    path('stratified/<str:api_key>', views.stratified_sampling, name='stratified_sampling'),
    path('systematic/<str:api_key>', views.systematic_sampling, name='systematic_sampling'),
    path('simple_random/<str:api_key>', views.simple_random_sampling, name='simple_random_sampling'),
    path('cluster_sampling/<str:api_key>', views.cluster_sampling, name='cluster_sampling'),
    path('purposive_sampling/<str:api_key>', views.purposive_sampling, name='purposive_sampling'),
    path('quote_sampling/<str:api_key>', views.quota_sampling, name='quota_sampling')
]
