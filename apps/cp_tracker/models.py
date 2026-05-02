from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class CPEntry(models.Model):
    CATEGORY_CHOICES = [
        ('exercise', 'Exercise'),
        ('diet', 'Diet'),
        ('sleep', 'Sleep'),
        ('meditation', 'Meditation'),
        ('reading', 'Reading'),
        ('goal', 'Goal'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cp_entries')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='goal')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    progress = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text='Progress percentage (0-100)'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name = 'CP Entry'
        verbose_name_plural = 'CP Entries'

    def __str__(self):
        return f'{self.title} - {self.date}'

    def get_absolute_url(self):
        return reverse('cp_tracker:detail', kwargs={'pk': self.pk})


class CPStreak(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cp_streak')
    current_streak = models.IntegerField(default=0)
    longest_streak = models.IntegerField(default=0)
    last_completed_date = models.DateField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - Streak: {self.current_streak}'

    class Meta:
        verbose_name = 'CP Streak'
        verbose_name_plural = 'CP Streaks'
