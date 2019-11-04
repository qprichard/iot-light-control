from classes.mqtt import MQTT
import paho.mqtt.client as mqtt
import json

from classes.nfc_reader import NFCReader
from public.config import BROKER_PWD, BROKER_USR, SERVER_URL, TOPIC_BASE, CLIENT_ID


nfc = NFCReader()

def on_message(client, userdata, message):
    msg = message.payload.decode('utf-8')
    msg = json.loads(msg)

    print(msg)

    client.loop.stop()
    client.unsubscribe(f"{TOPIC_BASE}/validateAuthentication")

#setup the mqtt client
mqtt_client = mqtt.Client(CLIENT_ID, True)
mqtt_client.username_pw_set(username=BROKER_USR, password=BROKER_PWD)
mqtt_client.on_message = on_message
mqtt_client.connect(SERVER_URL)

def on_reading(uid):
    msg = {
        'flag':'authentication'
        'card_uid': uid,
        'response_topic': f"{TOPIC_BASE}/validateAuthentication",
    }

    msg = json.dumps(msg)
    mqtt_client.publish(f"{TOPIC_BASE}/authentication", msg)
    mqtt_client.subscribe(f"{TOPIC_BASE}/validateAuthentication")
    mqtt_client.loop()

nfc.listen(on_reading=on_reading)
