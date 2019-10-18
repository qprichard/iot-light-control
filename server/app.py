import paho.mqtt.client as mqtt

from public.config import BROKER_PWD, BROKER_USR, HOST

def on_message(client, userdata, message):
    msg = message.payload.decode('utf-8')
    print(msg)

server = mqtt.Client('server')

server.on_message = on_message
server.username_pw_set(username=BROKER_USR, password=BROKER_PWD)
server.connect(HOST)
server.subscribe('iot-light-control/authentication')

server.loop_forever()
