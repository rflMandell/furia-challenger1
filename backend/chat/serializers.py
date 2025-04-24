from rest_framework import serializers
from .models import Chat, Message
from core.serializers import UserSerializer

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'name', 'slug']

class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'chat', 'user', 'content', 'timestamp']
        read_only_fields = ['user', 'timestamp']