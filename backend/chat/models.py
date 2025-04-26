from django.db import models
from core.models import User 
from django.contrib.auth import get_user_model

# Create your models here.

class Chat(models.Model):
    name = models.CharField(max_length=100) #nome do chat, vai ta como cs, lol etc...
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    upvote = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name="messages", on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    
    is_highlighted = models.BooleanField(default=Falde)
    
    def __str__(self):
        return f"Message {self.content[:20]} from {self.sender.username} in {self.chat.name}"
    
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey('Message', on_delete=models.CASCADE, related_name='votes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'message')

    def __str__(self):
        return f"{self.user.username} votou na mensagem {self.message.id}"