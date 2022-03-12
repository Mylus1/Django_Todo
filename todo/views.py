from django.shortcuts import render

from .models import Todo

# user creation example
# user = User.objects.create_user(username, email, password)


def index(request):
    context = {"todos": Todo.objects.all()}
    return render(request, "todo/index.html", context)


def create_todo(request):
    return render(request, "todo/create_todo.html")


def sign_up(request):
    return render(request, "todo/sign_up.html")
