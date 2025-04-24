from django.db import models
from core.models import User #impor do modelo de user do core

# Create your models here.

class Chat(models.Model):
    name = models.CharField(max_length=100) #nome do chat, vai ta como cs, lol etc...
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name="messages", on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.sender.username} in {self.chat.name}"