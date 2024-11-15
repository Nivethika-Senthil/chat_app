# chat/views.py
from django.shortcuts import render
from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer

# View for handling message CRUD via API
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

# View for rendering the chat room page
def chat_room(request):
    return render(request, 'chat/chat_room.html')
# chat/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ChatMessage
from .serializers import ChatMessageSerializer

class ChatMessageView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ChatMessageSerializer(data=request.data)
        
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response(
                    {"error": "Failed to save message.", "details": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
