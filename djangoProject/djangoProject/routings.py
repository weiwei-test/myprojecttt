# backend/routing.py

from django.urls import path
from myvue import consumers

websocket_urlpatterns = [
    path(r'ws/chat/', consumers.ChatConsumer.as_asgi()),
    path(r'order/chat/', consumers.OrderConsumer.as_asgi()),
]
