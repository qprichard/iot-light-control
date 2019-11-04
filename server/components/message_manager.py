"""
A class to handle the message you get by mqtt and send a response if usefull
"""

import paho.mqtt.client as mqtt
import json

from public.config import BROKER_PWD, BROKER_USR

class MessageManager():
    def __init__(self, client, payload):
        self.client = client
        self.payload = payload

        self.action = self.payload.get('action', None)
        del self.payload['action']
        self.response_topic = self.payload.get('response_topic', None)

        if self.response_topic is not None and self.action is not None:
            del self.payload['response_topic']
            self.send_response()

        elif self.action is not None:
            self.action(self.payload)

    def send_response(self):
        response = self.action(self.payload)
        response = json.dumps(response)
        self.client.publish(self.response_topic, response)
