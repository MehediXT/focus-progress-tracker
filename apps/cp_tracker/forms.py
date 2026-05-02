from django import forms
from .models import CPEntry


class CPEntryForm(forms.ModelForm):
    class Meta:
        model = CPEntry
        fields = ('category', 'title', 'description', 'completed', 'progress')
        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Entry title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Description',
                'rows': 4
            }),
            'completed': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4'
            }),
            'progress': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'type': 'range',
                'min': '0',
                'max': '100',
                'step': '1'
            }),
        }
