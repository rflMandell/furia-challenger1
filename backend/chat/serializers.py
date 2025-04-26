from rest_framework import serializers
from .models import Chat, Message, Vote
from core.serializers import UserSerializer

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'name', 'description', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'chat', 'user', 'content', 'created_at', 'upvotes', 'downvotes', 'is_highlighted']
        read_only_fields = ['user', 'created_at', 'chat']
        
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'user', 'message', 'created_at']