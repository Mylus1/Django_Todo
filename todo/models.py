from django.db import models
from datetime import timedelta, timezone
from django.urls import reverse

def placeholder_date():
    return timezone.now() + timezone.timedelta(days=7)

class TodoList(models.Model):
    title = models.CharField(max_length=150)
    
    def get_absolute_url(self):
        return reverse("lists" args=[self.id])

class TodoItem(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    todo_complete = models.BooleanField(default=False)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title} [{self.todo_complete}: due {self.placeholder_date}]"
    
