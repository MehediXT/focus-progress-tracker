from django.contrib import admin
from .models import StudyEntry, Subject, StudyGoal


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')
    search_fields = ('name', 'user__username')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(StudyEntry)
class StudyEntryAdmin(admin.ModelAdmin):
    list_display = ('topic', 'user', 'subject', 'date', 'duration', 'difficulty')
    list_filter = ('subject', 'difficulty', 'date')
    search_fields = ('topic', 'user__username', 'notes')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(StudyGoal)
class StudyGoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'daily_minutes', 'weekly_minutes', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
