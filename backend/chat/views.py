from rest_framework import viewsets, permissions, status, generics, filters, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Chat, Message, Vote
from .serializers import ChatSerializer, MessageSerializer, VoteSerializer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
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
        
class VoteChatView(APIView):
    def post(self, request, chat_id):
        chat = get_object_or_404(Chat, id=chat_id)
        vote_type = request.data.get('vote')
        
        if vote_type == 'upvote':
            chat.upvote += 1
        elif vote_type == 'downvote':
            chat.downvotes += 1
        else:
            return Response({'error': 'Tipo de voto invalido.'}, status=status.HTTP_400_BAD_REQUEST)
        
        chat.save()
        return Response({'message': 'Voto registrado com sucesso.'}, status=status.HTTP_200_OK)
        
class ChatListView(generics.ListAPIView):
    """
    vai exibir todos os chats tematicos disponiveis aqui
    """ 
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    
class MessageCreateView(generics.CreateAPIView):
    """ 
    Permite que o envio de uman mova mensagem para um chat tematico
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    def perform_create(self, serializer):
        chat_id = self.kwargs['chat_id']
        chat = Chat.objects.get(id=chat_id)
        serializer.save(chat=chat, user=self.request.user)
        
class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    
    filter_backends = [filters.OrderingFilter]
    ordering = ['-created_at'] #msg mais recente primeiro
    
    def get_queryset(self):
        queryset = super().get_queryset()
        chat_id = self.kwargs['chat_id']
        
        if chat_id:
            queryset = queryset.filter(chat_id=chat_id)
            
        return queryset
    
class HighlightMessageView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, message_id):
        #verifica se e um adm
        if not request.user.is_staff:
            return Response({'error': 'Voce nao tem permissao para destacar mensagens.'},
                            status=status.HTTP_403_FORBIDDEN)
        
        message = get_object_or_404(Message, id=message_id)
        
        # tira o destaque de outras msgs do mesmo chat
        Message.objects.filter(chat=message.chat, is_highlighted=True).update(is_highlighted=False)
        
        # agr destaca a msg atual
        message.is_highlighted = True
        message.save()
        
        return Response({'message': 'Messagem destacada com sucesso.'}, status=status.HTTP_200_OK)
    
class RemoveHighlightMessageView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, message_id):
        try:
            message = Message.objects.get(id=message_id)
        except Message.DoesNotExist:
            return Response({"detail": "messagem nao encontrada."}, status=status.HTTP_404_NOT_FOUND)
        
        message.is_highlighted = False
        message.save()
        
        return Response({"detail": "destaque removido com sucesso."}, status=status.HTTP_200_OK)
        

def online_users_view(request):
    return JsonResponse({"online_users": get_online_users()})