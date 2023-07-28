from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('API.urls')),
    path('sample-size/', include('SampleSizeApi.urls'))
    
]
