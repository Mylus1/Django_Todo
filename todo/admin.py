from django.contrib import admin

from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "start_date", "todo_complete", "priority")
    fields = ("title", "description", "todo_complete", "start_date", "priority")
    readonly_fields = ("start_date",)
    list_filter = ("todo_complete", "priority")

admin.site.register(Todo, TodoAdmin)
