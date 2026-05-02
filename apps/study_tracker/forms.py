from django import forms
from .models import StudyEntry, Subject, StudyGoal


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('name', 'description', 'color')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Subject name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Subject description',
                'rows': 3
            }),
            'color': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'type': 'color'
            }),
        }


class StudyEntryForm(forms.ModelForm):
    class Meta:
        model = StudyEntry
        fields = ('subject', 'topic', 'notes', 'difficulty', 'duration', 'rating')
        widgets = {
            'subject': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'topic': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Topic studied'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Study notes',
                'rows': 4
            }),
            'difficulty': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'duration': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Duration in minutes',
                'type': 'number',
                'min': '0'
            }),
            'rating': forms.RadioSelect(attrs={
                'class': 'me-2'
            }),
        }


class StudyGoalForm(forms.ModelForm):
    class Meta:
        model = StudyGoal
        fields = ('daily_minutes', 'weekly_minutes')
        widgets = {
            'daily_minutes': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Daily target in minutes',
                'type': 'number',
                'min': '0'
            }),
            'weekly_minutes': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Weekly target in minutes',
                'type': 'number',
                'min': '0'
            }),
        }
