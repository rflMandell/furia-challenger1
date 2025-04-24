from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        chat_id = self.request.query_params.get('chat')
        if chat_id:
            return Message.objects.filter(chat_id=chat_id)
        return Message.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)