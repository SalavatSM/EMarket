import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import User


class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('mygroup', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('mygroup', self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        if message['type'] == 'new_user':
            # отправка сообщения всем в группе
            await self.channel_layer.group_send('mygroup', {
                'type': 'chat_message',
                'message': f'Created new user: {message["username"]}'
            })
        # Здесь вы можете обрабатывать полученные сообщения
        # Например, отправлять уведомления всем подключенным клиентам

        # Отправка сообщения всем в группе

        await self.channel_layer.group_send('mygroup', {
            'type': 'chat_message',
            'message': message
        })

    async def chat_message(self, event):
        message = event['message']
        # Отправка сообщения клиенту
        await self.send(text_data=json.dumps({
            'message': message
        }))


