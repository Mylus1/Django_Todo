from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from .models import Todo
from .serializers import Todo_Serializer
from django.template import loader
from django.shortcuts import render
import django.db
from django.contrib.auth.models import User



# user = User.objects.create_user(username, email, password)


class Todo_FullList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todo_Serializer
   
class Todo_Edit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todo_Serializer
     
def index(request):
    context = {
        'todos': Todo.objects.all()
    }
    return render(request, "todo/index.html", context)

def create(request):
    return render(request, "todo/form.html")

def sign_up(request):
    return render (request, "todo/sign_up.html")