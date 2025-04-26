from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Chat(models.Model):
    CHAT_CHOICE = [
        ('cs', 'Counter Strike'),
        ('lol', 'League of Legends'),
        ('valorant', 'Valorant'),
        ('kings_league', "King's League"),
        ('general', 'Chat Geral'),
    ]
    
    name = models.CharField(max_length=50, choices=CHAT_CHOICE, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.get_name_display()

class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"