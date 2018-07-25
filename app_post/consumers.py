from channels.generic.websocket import WebsocketConsumer
import json

class NewPostConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
    
    def disconect(self, close_code):
        pass
    
    def recive(self, text_data='None data. WTF'):
        # text_data_json = json.loads(text_data)
        self.send(text_data="Hello Roman (=")


    def notify(self, msg):
        self.send(text_data=json.dumps({
            'newId': msg['newId']
        }))
    