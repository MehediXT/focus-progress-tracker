from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'completed', 'created_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('title', 'user__username')
    readonly_fields = ('created_at', 'completed_at')
    fieldsets = (
        ('Task Info', {
            'fields': ('user', 'title', 'description')
        }),
        ('Status', {
            'fields': ('completed', 'completed_at')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
