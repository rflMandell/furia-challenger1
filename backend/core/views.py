from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAdminUser
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        instance = serializer.save()
        if 'is_highlighted' in self.request.data:
            instance.is_highlighted = self.request.data['is_highlighted']
            instance.save()