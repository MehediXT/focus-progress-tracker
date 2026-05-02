from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from apps.cp_tracker.models import CPEntry
from apps.deen_tracker.models import DeenEntry
from apps.study_tracker.models import StudyEntry
from .models import Todo
from .forms import TodoForm


class DashboardView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def get(self, request):
        user = request.user
        
        # Get latest entries from each tracker
        cp_entries = CPEntry.objects.filter(user=user).order_by('-date')[:5]
        deen_entries = DeenEntry.objects.filter(user=user).order_by('-date')[:5]
        study_entries = StudyEntry.objects.filter(user=user).order_by('-date')[:5]
        
        # Calculate stats
        cp_total = CPEntry.objects.filter(user=user).count()
        deen_total = DeenEntry.objects.filter(user=user).count()
        study_total = StudyEntry.objects.filter(user=user).count()
        
        # Get todos
        todos = Todo.objects.filter(user=user, completed=False)
        completed_todos = Todo.objects.filter(user=user, completed=True).count()
        todo_form = TodoForm()
        
        context = {
            'cp_entries': cp_entries,
            'deen_entries': deen_entries,
            'study_entries': study_entries,
            'cp_total': cp_total,
            'deen_total': deen_total,
            'study_total': study_total,
            'todos': todos,
            'completed_todos': completed_todos,
            'todo_form': todo_form,
        }
        
        return render(request, 'dashboard.html', context)

    def post(self, request):
        user = request.user
        form = TodoForm(request.POST)
        
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
        
        return redirect('dashboard')


@require_http_methods(["POST"])
def toggle_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        todo.completed = not todo.completed
        if todo.completed:
            todo.completed_at = timezone.now()
        else:
            todo.completed_at = None
        todo.save()
        
        return JsonResponse({
            'success': True,
            'completed': todo.completed,
            'completed_at': todo.completed_at.strftime('%Y-%m-%d %H:%M') if todo.completed_at else None
        })
    
    return redirect('dashboard')


@require_http_methods(["POST"])
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        todo.delete()
        return JsonResponse({'success': True})
    
    return redirect('dashboard')
