from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class DeenEntry(models.Model):
    ACTIVITY_CHOICES = [
        ('salah', 'Salah (Prayer)'),
        ('quran', 'Quran Recitation'),
        ('dhikr', 'Dhikr'),
        ('dua', 'Dua (Supplication)'),
        ('charity', 'Charity'),
        ('knowledge', 'Islamic Knowledge'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='deen_entries')
    activity = models.CharField(max_length=20, choices=ACTIVITY_CHOICES, default='salah')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    reflection = models.TextField(blank=True, help_text='Personal reflection or notes')
    date = models.DateField(auto_now_add=True)
    duration = models.IntegerField(default=0, help_text='Duration in minutes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name = 'Deen Entry'
        verbose_name_plural = 'Deen Entries'

    def __str__(self):
        return f'{self.title} - {self.date}'

    def get_absolute_url(self):
        return reverse('deen_tracker:detail', kwargs={'pk': self.pk})


class DeenGoal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='deen_goal')
    daily_target = models.CharField(
        max_length=255,
        blank=True,
        help_text='Your daily deen goal'
    )
    weekly_target = models.CharField(
        max_length=255,
        blank=True,
        help_text='Your weekly deen goal'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - Deen Goals'

    class Meta:
        verbose_name = 'Deen Goal'
        verbose_name_plural = 'Deen Goals'
