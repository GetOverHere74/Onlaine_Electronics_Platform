from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('online_platform.urls', namespace='online_platform')),
    path("users/", include("users.urls", namespace="users")),
]
