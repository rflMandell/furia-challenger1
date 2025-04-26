from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Chat, Message, Vote
from .serializers import ChatSerializer, MessageSerializer, VoteSerializer
from django.http import JsonResponse
from .online_users import get_online_users

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

class MessageViewSet(viewsets.ModelViewSet):
    # Definindo o queryset
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        chat_id = self.request.query_params.get('chat')
        if chat_id:
            return Message.objects.filter(chat_id=chat_id)
        return Message.objects.all()

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
        
class VoteViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    def create(self, request):
        message_id = request.data.get('message')
        try:
            message = Message.objects.get(id=message_id)
        except Message.DoesNotExist:
            return Response({"error": "Mensagem nao encontrada"}, status=status.HTTP_400_BAD_REQUEST)
        
        vote, created = Vote.objects.get_or_create(user=request.user, message=message)
        
        if not created:
            return Response({"error": "Voce ja votou nessa mensagem"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = VoteSerializer(vote)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk=None):
        try:
            vote = Vote.objects.get(id=pk, user=request.user)
            vote.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Vote.DoesNotExist:
            return Response({"error": "Voto nao encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        
        

def online_users_view(request):
    return JsonResponse({"online_users": get_online_users()})