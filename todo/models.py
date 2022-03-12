from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    todo_complete = models.BooleanField(default=False)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title} [{self.todo_complete}]"
