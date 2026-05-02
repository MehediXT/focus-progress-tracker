from django.urls import path
from .views import DashboardView, toggle_todo, delete_todo

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('todo/<int:todo_id>/toggle/', toggle_todo, name='toggle_todo'),
    path('todo/<int:todo_id>/delete/', delete_todo, name='delete_todo'),
]

#hello 