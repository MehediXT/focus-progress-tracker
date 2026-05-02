from django.contrib import admin
from .models import CPEntry, CPStreak


@admin.register(CPEntry)
class CPEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'date', 'completed', 'progress')
    list_filter = ('category', 'completed', 'date')
    search_fields = ('title', 'user__username', 'description')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(CPStreak)
class CPStreakAdmin(admin.ModelAdmin):
    list_display = ('user', 'current_streak', 'longest_streak', 'last_completed_date')
    readonly_fields = ('updated_at',)
