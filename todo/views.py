from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from .models import Todo
from .serializers import Todo_Serializer


class Todo_FullList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todo_Serializer
   
class Todo_Edit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todo_Serializer
     