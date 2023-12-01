from django.contrib import admin

from .models import (
    headings,
    tasks
)

class TaskInLine(admin.TabularInline): 
    model = tasks.Task

class HeadingAdmin(admin.ModelAdmin):
    ordering = ["created"]
    inlines = [
        TaskInLine
    ]

class TaskAdmin(admin.ModelAdmin):
    list_display = ["task", "created", "updated"]
    ordering = ["created"]
    raw_id_fields = ["heading"]
    
admin.site.register(headings.Heading, HeadingAdmin)
admin.site.register(tasks.Task, TaskAdmin)