from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import TodoItem
from .serializers import TodoItemSerializer

class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
