from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Subject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='study_subjects')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=7, default='#3b82f6', help_text='Hex color code')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        unique_together = ('user', 'name')

    def __str__(self):
        return f'{self.name} - {self.user.username}'


class StudyEntry(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='study_entries')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='entries')
    topic = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')
    duration = models.IntegerField(default=0, help_text='Study duration in minutes')
    date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=3, choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name = 'Study Entry'
        verbose_name_plural = 'Study Entries'

    def __str__(self):
        return f'{self.topic} - {self.date}'

    def get_absolute_url(self):
        return reverse('study_tracker:detail', kwargs={'pk': self.pk})


class StudyGoal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='study_goal')
    daily_minutes = models.IntegerField(default=60, help_text='Daily study target in minutes')
    weekly_minutes = models.IntegerField(default=420, help_text='Weekly study target in minutes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - Study Goals'

    class Meta:
        verbose_name = 'Study Goal'
        verbose_name_plural = 'Study Goals'
