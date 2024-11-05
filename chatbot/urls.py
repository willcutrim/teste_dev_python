from django.urls import path
from .views import chat_view, get_all_chats

urlpatterns = [
    path('chat/', chat_view, name='chatbot'),
    path('get_chats/', get_all_chats, name='get_chats'),
]