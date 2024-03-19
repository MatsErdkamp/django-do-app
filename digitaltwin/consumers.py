# consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Counter
from asgiref.sync import sync_to_async
import json


class CounterConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.counter, _ = await sync_to_async(Counter.objects.get_or_create, thread_sensitive=True)(id=1)
        await self.accept()
        await self.send_count_update()

    async def disconnect(self, close_code):
        pass

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json['action']
        
        if action == 'increment':
            await self.increment_counter()
        elif action == 'decrement':
            await self.decrement_counter()
        
        await self.send_count_update()

    @sync_to_async
    def increment_counter(self):
        self.counter.count += 1
        self.counter.save()

    @sync_to_async
    def decrement_counter(self):
        self.counter.count -= 1
        self.counter.save()
    
    async def send_count_update(self):
        await self.send(text_data=json.dumps({
            'count': self.counter.count
        }))