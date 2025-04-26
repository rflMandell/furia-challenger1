from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChatViewSet, MessageViewSet, online_users_view, VoteViewSet, ChatListView, MessageCreateView, MessageListView, VoteChatView, HighlightMessageView

router = DefaultRouter()
router.register(r'chats', ChatViewSet)     
router.register(r'messages', MessageViewSet)
router.register(r'votes', VoteViewSet, basename='vote')

urlpatterns = [
    path('', include(router.urls)),
    path('online-users/', online_users_view),
    path('chats/', ChatListView.as_view(), name='chat-list'),
    path('chats/<int:chat_id>/messages/', MessageCreateView.as_view(), name='send-message'),
    path('chats/<int:chat_id>/messages/', MessageListView.as_view(), name='message-list'),
    path('chats/<int:chat_id>/vote/', VoteChatView.as_view(), name='chat-vote'),
    path('messages/<int:message_id>/highlight/', HighlightMessageView.as_view(), name='highlight-message'),
    path('messages/', MessageListView.as_view(), name='message-list'),
]

urlpatterns += router.urls