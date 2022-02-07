from rest_framework import serializers
from .models import Todo

class Todo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
