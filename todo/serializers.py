from rest_framework import serializers
from .models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['id', 'user', 'title', 'description', 'status', 'created_at', 'updated_at']
        read_only_fields = ['user']  