from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    re_path(r"pms/ws/$", consumers.EchoConsumer.as_asgi()),
]