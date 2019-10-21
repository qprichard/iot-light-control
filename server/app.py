import paho.mqtt.client as mqtt
import json

from public.config import BROKER_PWD, BROKER_USR, HOST, TOPIC_BASE
from components.message_manager import MessageManager

def action(data):
    data['authorization'] = "granted"
    return data

def on_message(client, userdata, message):
    #decode message to have a dict
    msg = message.payload.decode('utf-8')
    msg = json.loads(msg)
    msg['action'] = action
    
    MessageManager(client, msg)
server = mqtt.Client('server')

server.on_message = on_message
server.username_pw_set(username=BROKER_USR, password=BROKER_PWD)
server.connect(HOST)
server.subscribe(f"{TOPIC_BASE}/authentication")
server.loop_forever()
