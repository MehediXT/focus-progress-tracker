from django.urls import path
from .views import (
    DeenDashboardView, DeenDetailView, DeenCreateView,
    DeenUpdateView, DeenDeleteView, DeenGoalView
)

app_name = 'deen_tracker'

urlpatterns = [
    path('', DeenDashboardView.as_view(), name='dashboard'),
    path('<int:pk>/', DeenDetailView.as_view(), name='detail'),
    path('create/', DeenCreateView.as_view(), name='create'),
    path('<int:pk>/update/', DeenUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', DeenDeleteView.as_view(), name='delete'),
    path('goals/', DeenGoalView.as_view(), name='goals'),
]
