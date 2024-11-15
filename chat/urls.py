# chat/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Setting up the router for the API endpoints
router = DefaultRouter()
router.register(r'messages', views.MessageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # API endpoint for CRUD operations
    path('chat/', views.chat_room, name='chat_room'),  # Web page for chat
]
