from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('git_service.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
