from channels.generic.websocket import WebsocketConsumer
import json

class NewPostConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
    
    def disconect(self, close_code):
        pass

    def notify(self, msg):
        self.send(text_data=json.dumps({
            'newId': msg['newId']
        }))
    