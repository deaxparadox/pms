from django.contrib.auth.models import User 
from channels.consumer import AsyncConsumer
from asgiref.sync import sync_to_async
import json

@sync_to_async
def get_all_users():
    return User.objects.all()

class EchoConsumer(AsyncConsumer):
    """
    Convert the data  to JSON strings, before sending
    """
    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, event):
        users = await get_all_users()
        users_name = [x.username for x in users]
        await self.send({
            "type": "websocket.send",
            "text": json.dumps(users_name),
        })