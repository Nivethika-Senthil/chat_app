from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'messages', views.MessageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # API routes
    path('chat/', views.chat_room, name='chat_room'),  # Chat room page
]
