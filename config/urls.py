"""
URL configuration for Focus-Life-Tracker project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.users.urls', namespace='users')),
    path('', include('apps.dashboard.urls', namespace='dashboard')),
    path('cp/', include('apps.cp_tracker.urls', namespace='cp_tracker')),
    path('deen/', include('apps.deen_tracker.urls', namespace='deen_tracker')),
    path('study/', include('apps.study_tracker.urls', namespace='study_tracker')),
]
