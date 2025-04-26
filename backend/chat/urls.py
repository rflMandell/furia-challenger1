from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChatViewSet, MessageViewSet, online_users_view

router = DefaultRouter()
router.register(r'chats', ChatViewSet)     
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('online-users/', online_users_view),
]