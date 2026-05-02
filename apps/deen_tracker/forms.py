from django import forms
from .models import DeenEntry, DeenGoal


class DeenEntryForm(forms.ModelForm):
    class Meta:
        model = DeenEntry
        fields = ('activity', 'title', 'description', 'reflection', 'duration')
        widgets = {
            'activity': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Entry title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Description',
                'rows': 3
            }),
            'reflection': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Your reflections and thoughts',
                'rows': 4
            }),
            'duration': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Duration in minutes',
                'type': 'number',
                'min': '0'
            }),
        }


class DeenGoalForm(forms.ModelForm):
    class Meta:
        model = DeenGoal
        fields = ('daily_target', 'weekly_target')
        widgets = {
            'daily_target': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'What is your daily deen goal?',
                'rows': 3
            }),
            'weekly_target': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'What is your weekly deen goal?',
                'rows': 3
            }),
        }
