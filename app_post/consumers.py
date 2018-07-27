from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class NewPostConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = 'posts_main'

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        
        self.accept()
       
    def disconect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )
    
    def notify(self, data):
        self.send(text_data=json.dumps({
            'newId': data['id']
        }))
    