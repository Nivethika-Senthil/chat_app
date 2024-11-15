# chat/serializers.py
from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'content', 'timestamp']
# chat/serializers.py

from rest_framework import serializers
from .models import ChatMessage

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'
    
    def validate_message(self, value):
        if not value.strip():  # Ensure the message is not empty
            raise serializers.ValidationError("Message cannot be empty.")
        return value
