from django.shortcuts import render

from rest_framework import viewsets
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated] #faz com que o user esteja autenticado
    
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated] #mesma coisa que a class de cima
    
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)