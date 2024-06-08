from django.contrib import admin
from django.urls import path, include  # Import include to include the API URLs

urlpatterns = [
    path('', include('api.urls')),  # Include the API URLs
    path('admin/', admin.site.urls),
]
