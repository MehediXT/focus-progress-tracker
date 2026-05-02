from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Sum
from .models import StudyEntry, Subject, StudyGoal
from .forms import StudyEntryForm, SubjectForm, StudyGoalForm


class StudyDashboardView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def get(self, request):
        user = request.user
        subjects = Subject.objects.filter(user=user)
        entries = StudyEntry.objects.filter(user=user).order_by('-date', '-created_at')[:10]
        goal, _ = StudyGoal.objects.get_or_create(user=user)
        
        # Calculate total study time
        total_minutes = StudyEntry.objects.filter(user=user).aggregate(
            total=Sum('duration')
        )['total'] or 0
        
        context = {
            'subjects': subjects,
            'entries': entries,
            'goal': goal,
            'total_minutes': total_minutes,
            'total_hours': round(total_minutes / 60, 1),
        }
        return render(request, 'study_tracker/study_dashboard.html', context)


class StudyDetailView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def get(self, request, pk):
        entry = get_object_or_404(StudyEntry, pk=pk, user=request.user)
        return render(request, 'study_tracker/study_detail.html', {'entry': entry})


class StudyCreateView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def get(self, request):
        form = StudyEntryForm()
        form.fields['subject'].queryset = Subject.objects.filter(user=request.user)
        return render(request, 'study_tracker/study_form.html', {'form': form, 'action': 'Create'})

    def post(self, request):
        form = StudyEntryForm(request.POST)
        form.fields['subject'].queryset = Subject.objects.filter(user=request.user)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            messages.success(request, 'Study entry created successfully!')
            return redirect('study_tracker:dashboard')
        return render(request, 'study_tracker/study_form.html', {'form': form, 'action': 'Create'})


class StudyUpdateView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def get(self, request, pk):
        entry = get_object_or_404(StudyEntry, pk=pk, user=request.user)
        form = StudyEntryForm(instance=entry)
        form.fields['subject'].queryset = Subject.objects.filter(user=request.user)
        return render(request, 'study_tracker/study_form.html', {'form': form, 'entry': entry, 'action': 'Update'})

    def post(self, request, pk):
        entry = get_object_or_404(StudyEntry, pk=pk, user=request.user)
        form = StudyEntryForm(request.POST, instance=entry)
        form.fields['subject'].queryset = Subject.objects.filter(user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Study entry updated successfully!')
            return redirect('study_tracker:detail', pk=pk)
        return render(request, 'study_tracker/study_form.html', {'form': form, 'entry': entry, 'action': 'Update'})


class StudyDeleteView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def post(self, request, pk):
        entry = get_object_or_404(StudyEntry, pk=pk, user=request.user)
        entry.delete()
        messages.success(request, 'Study entry deleted successfully!')
        return redirect('study_tracker:dashboard')


class SubjectCreateView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def get(self, request):
        form = SubjectForm()
        return render(request, 'study_tracker/subject_form.html', {'form': form, 'action': 'Create'})

    def post(self, request):
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.user = request.user
            subject.save()
            messages.success(request, 'Subject created successfully!')
            return redirect('study_tracker:dashboard')
        return render(request, 'study_tracker/subject_form.html', {'form': form, 'action': 'Create'})


class SubjectUpdateView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def get(self, request, pk):
        subject = get_object_or_404(Subject, pk=pk, user=request.user)
        form = SubjectForm(instance=subject)
        return render(request, 'study_tracker/subject_form.html', {'form': form, 'subject': subject, 'action': 'Update'})

    def post(self, request, pk):
        subject = get_object_or_404(Subject, pk=pk, user=request.user)
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subject updated successfully!')
            return redirect('study_tracker:dashboard')
        return render(request, 'study_tracker/subject_form.html', {'form': form, 'subject': subject, 'action': 'Update'})


class SubjectDeleteView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def post(self, request, pk):
        subject = get_object_or_404(Subject, pk=pk, user=request.user)
        subject.delete()
        messages.success(request, 'Subject deleted successfully!')
        return redirect('study_tracker:dashboard')


class StudyGoalView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def get(self, request):
        goal, _ = StudyGoal.objects.get_or_create(user=request.user)
        form = StudyGoalForm(instance=goal)
        return render(request, 'study_tracker/study_goal.html', {'form': form})

    def post(self, request):
        goal, _ = StudyGoal.objects.get_or_create(user=request.user)
        form = StudyGoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Study goals updated successfully!')
            return redirect('study_tracker:dashboard')
        return render(request, 'study_tracker/study_goal.html', {'form': form})
