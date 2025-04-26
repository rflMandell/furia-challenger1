from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

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
    path('messages/', MessageListView.as_view(), name='message-list'),
    path('messages/<int:message_id>/highlight/', HighlightMessageView.as_view(), name='highlight-message'),
    path('messages/<int:message_id>/remove-highlight/', RemoveHighlightMessageView.as_view(), name='remove-highlight-message'),
    path('chats/highlighted/', ChatsWithHighlightedMessagesView.as_view(), name='chats-with-highlighted-messages'),
    path('chats/<int:chat_id>/messages/', MessagesByChatView.as_view(), name='messages-by-chat'),
    path('chats/<int:chat_id>/messages_with_votes/', MessagesWithVotesByChatViews.as_view(), name='messages-with-votes-by-chat'),
    path('chats/summary/', ChatSummaryView.as_view(), name='chat-summary'),
    path('chats/summary/export/', ChatSummaryExportView.as_view(), name='chat-summary-export'),
]

urlpatterns += router.urls