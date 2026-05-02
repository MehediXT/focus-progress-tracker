from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import DeenEntry, DeenGoal
from .forms import DeenEntryForm, DeenGoalForm


class DeenDashboardView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def get(self, request):
        user = request.user
        entries = DeenEntry.objects.filter(user=user).order_by('-date', '-created_at')[:10]
        goal, _ = DeenGoal.objects.get_or_create(user=user)
        
        # Get activity statistics
        activities = {}
        for activity_code, activity_name in DeenEntry.ACTIVITY_CHOICES:
            activities[activity_name] = DeenEntry.objects.filter(
                user=user, activity=activity_code
            ).count()
        
        context = {
            'entries': entries,
            'goal': goal,
            'activities': activities,
        }
        return render(request, 'deen_tracker/deen_dashboard.html', context)


class DeenDetailView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def get(self, request, pk):
        entry = get_object_or_404(DeenEntry, pk=pk, user=request.user)
        return render(request, 'deen_tracker/deen_detail.html', {'entry': entry})


class DeenCreateView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def get(self, request):
        form = DeenEntryForm()
        return render(request, 'deen_tracker/deen_form.html', {'form': form, 'action': 'Create'})

    def post(self, request):
        form = DeenEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            messages.success(request, 'Deen entry created successfully!')
            return redirect('deen_tracker:dashboard')
        return render(request, 'deen_tracker/deen_form.html', {'form': form, 'action': 'Create'})


class DeenUpdateView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def get(self, request, pk):
        entry = get_object_or_404(DeenEntry, pk=pk, user=request.user)
        form = DeenEntryForm(instance=entry)
        return render(request, 'deen_tracker/deen_form.html', {'form': form, 'entry': entry, 'action': 'Update'})

    def post(self, request, pk):
        entry = get_object_or_404(DeenEntry, pk=pk, user=request.user)
        form = DeenEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Deen entry updated successfully!')
            return redirect('deen_tracker:detail', pk=pk)
        return render(request, 'deen_tracker/deen_form.html', {'form': form, 'entry': entry, 'action': 'Update'})


class DeenDeleteView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def post(self, request, pk):
        entry = get_object_or_404(DeenEntry, pk=pk, user=request.user)
        entry.delete()
        messages.success(request, 'Deen entry deleted successfully!')
        return redirect('deen_tracker:dashboard')


class DeenGoalView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def get(self, request):
        goal, _ = DeenGoal.objects.get_or_create(user=request.user)
        form = DeenGoalForm(instance=goal)
        return render(request, 'deen_tracker/deen_goal.html', {'form': form})

    def post(self, request):
        goal, _ = DeenGoal.objects.get_or_create(user=request.user)
        form = DeenGoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Deen goals updated successfully!')
            return redirect('deen_tracker:dashboard')
        return render(request, 'deen_tracker/deen_goal.html', {'form': form})
