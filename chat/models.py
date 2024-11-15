# chat/models.py
from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} -> {self.receiver}: {self.content}'
# chat/models.py



class ChatMessage(models.Model):
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    message = models.TextField()  # Ensure NOT NULL constraint by avoiding `blank=True` or `null=True`
    timestamp = models.DateTimeField(auto_now_add=True)