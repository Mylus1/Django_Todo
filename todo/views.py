from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Todo

# user creation example
# user = User.objects.create_user(username, email, password)


def index(request):
    context = {"todos": Todo.objects.all()}
    return render(request, "todo/index.html", context)


def create_todo(request):
    if request.method == "POST":
        Todo.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            priority=request.POST["priority"]
        )
        return HttpResponseRedirect(reverse("index"))

    return render(request, "todo/create_todo.html")


def sign_up(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST["username"],
            password=request.POST["password"],
            email=request.POST["email"]
        )
        return HttpResponseRedirect(reverse("index"))
    return render(request, "todo/sign_up.html")

def list_todos(request):
    if request.method == "GET":
        all_todos = Todo.objects()
        print(all_todos)
    return render(request, 'todo/list_todos.html')