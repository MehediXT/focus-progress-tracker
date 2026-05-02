from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import CPEntry, CPStreak
from .forms import CPEntryForm
from datetime import date, timedelta


class CPListView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def get(self, request):
        user = request.user
        entries = CPEntry.objects.filter(user=user).order_by('-date', '-created_at')
        
        # Get streak info
        streak, _ = CPStreak.objects.get_or_create(user=user)
        
        # Filter by category if provided
        category = request.GET.get('category')
        if category:
            entries = entries.filter(category=category)
        
        context = {
            'entries': entries,
            'streak': streak,
            'categories': CPEntry.CATEGORY_CHOICES,
            'selected_category': category,
        }
        return render(request, 'cp_tracker/cp_list.html', context)


class CPDetailView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def get(self, request, pk):
        entry = get_object_or_404(CPEntry, pk=pk, user=request.user)
        return render(request, 'cp_tracker/cp_detail.html', {'entry': entry})


class CPCreateView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def get(self, request):
        form = CPEntryForm()
        return render(request, 'cp_tracker/cp_form.html', {'form': form, 'action': 'Create'})

    def post(self, request):
        form = CPEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            messages.success(request, 'Entry created successfully!')
            return redirect('cp_tracker:list')
        return render(request, 'cp_tracker/cp_form.html', {'form': form, 'action': 'Create'})


class CPUpdateView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def get(self, request, pk):
        entry = get_object_or_404(CPEntry, pk=pk, user=request.user)
        form = CPEntryForm(instance=entry)
        return render(request, 'cp_tracker/cp_form.html', {'form': form, 'entry': entry, 'action': 'Update'})

    def post(self, request, pk):
        entry = get_object_or_404(CPEntry, pk=pk, user=request.user)
        form = CPEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entry updated successfully!')
            return redirect('cp_tracker:detail', pk=pk)
        return render(request, 'cp_tracker/cp_form.html', {'form': form, 'entry': entry, 'action': 'Update'})


class CPDeleteView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def post(self, request, pk):
        entry = get_object_or_404(CPEntry, pk=pk, user=request.user)
        entry.delete()
        messages.success(request, 'Entry deleted successfully!')
        return redirect('cp_tracker:list')
