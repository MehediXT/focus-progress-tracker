from django.urls import path
from .views import (
    CPListView, CPDetailView, CPCreateView, 
    CPUpdateView, CPDeleteView
)

app_name = 'cp_tracker'

urlpatterns = [
    path('', CPListView.as_view(), name='list'),
    path('<int:pk>/', CPDetailView.as_view(), name='detail'),
    path('create/', CPCreateView.as_view(), name='create'),
    path('<int:pk>/update/', CPUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CPDeleteView.as_view(), name='delete'),
]
