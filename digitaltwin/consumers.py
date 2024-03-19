import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Counter

class CounterConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'counter_updates'  # Name of the group for broadcasting messages
        self.counter, _ = await database_sync_to_async(Counter.objects.get_or_create, thread_sensitive=True)(id=1)
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        await self.send_count_update()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json['action']
        
        if action == 'increment':
            await self.increment_counter()
        elif action == 'decrement':
            await self.decrement_counter()
        
        await self.send_count_update_broadcast()

    @database_sync_to_async
    def increment_counter(self):
        self.counter.count += 1
        self.counter.save()

    @database_sync_to_async
    def decrement_counter(self):
        self.counter.count -= 1
        self.counter.save()
    
    async def send_count_update(self):
        # Send message to WebSocket client
        await self.send(text_data=json.dumps({
            'count': self.counter.count
        }))

    async def send_count_update_broadcast(self):
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'count_update',
                'count': self.counter.count
            }
        )

    # Receive message from room group
    async def count_update(self, event):
        count = event['count']
        
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'count': count
        }))
