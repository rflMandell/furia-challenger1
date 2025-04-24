from rest_framework import serializers
from .models import Chat, Message
from core.models import User

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'name', 'description', 'created_at']
        
class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField() #vai exibir o nome do user que enviou a msg
    
    class Meta:
        model = Message
        fields = ['id', 'chat', 'sender', 'content', 'created_at']
