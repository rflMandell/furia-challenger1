from rest_framework import serializers
from .models import Chat, Message, Vote
from core.serializers import UserSerializer

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'name', 'description', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    vote_count = serializers.IntegerField(source='votes.count', read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'chat', 'sender', 'content', 'created_at', 'vote_count']
        read_only_fields = ['sender', 'created_at']
        
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'user', 'message', 'created_at']