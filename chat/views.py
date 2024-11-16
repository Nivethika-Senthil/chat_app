from django.shortcuts import render
from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer

# API View for CRUD operations
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-timestamp')
    serializer_class = MessageSerializer

# Render chat room
def chat_room(request):
    return render(request, 'chat/chat_room.html')
