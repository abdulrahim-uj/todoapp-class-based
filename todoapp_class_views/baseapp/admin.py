from django.contrib import admin
from . models import Task


# admin.site.register(Task)


class TaskAdmin(admin.ModelAdmin):
    # list_display = ('id', 'name', 'priority', 'status', 'created', 'is_deleted')
    list_display = ('id', 'name', 'priority', 'status', 'created')


admin.site.register(Task, TaskAdmin)
