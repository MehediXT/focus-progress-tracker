from django.urls import path
from .views import (
    StudyDashboardView, StudyDetailView, StudyCreateView,
    StudyUpdateView, StudyDeleteView, SubjectCreateView,
    SubjectUpdateView, SubjectDeleteView, StudyGoalView
)

app_name = 'study_tracker'

urlpatterns = [
    path('', StudyDashboardView.as_view(), name='dashboard'),
    path('<int:pk>/', StudyDetailView.as_view(), name='detail'),
    path('create/', StudyCreateView.as_view(), name='create'),
    path('<int:pk>/update/', StudyUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', StudyDeleteView.as_view(), name='delete'),
    path('subject/create/', SubjectCreateView.as_view(), name='subject_create'),
    path('subject/<int:pk>/update/', SubjectUpdateView.as_view(), name='subject_update'),
    path('subject/<int:pk>/delete/', SubjectDeleteView.as_view(), name='subject_delete'),
    path('goals/', StudyGoalView.as_view(), name='goals'),
]
