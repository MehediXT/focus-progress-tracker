from django.contrib import admin
from .models import DeenEntry, DeenGoal


@admin.register(DeenEntry)
class DeenEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'activity', 'date', 'duration')
    list_filter = ('activity', 'date')
    search_fields = ('title', 'user__username', 'description')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(DeenGoal)
class DeenGoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
