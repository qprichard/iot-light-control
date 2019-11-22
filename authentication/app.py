from classes.mqtt import MQTT
import paho.mqtt.client as mqtt
import json
import time

from classes.nfc_reader import NFCReader
from public.config import BROKER_PWD, BROKER_USR, SERVER_URL, TOPIC_BASE, CLIENT_ID



class RaspberryAuthentication():
    def __init__(self):
        self.nfc = NFCReader()
        self.loop_flag = 0

        self.mqtt_client = mqtt.Client(CLIENT_ID, True)
        self.mqtt_client.username_pw_set(username=BROKER_USR, password=BROKER_PWD)
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.connect(SERVER_URL)

        self.nfc.listen(on_reading=self.on_reading)

    def on_message(self, client, userdata, message):
        msg = message.payload.decode('utf-8')
        msg = json.loads(msg)

        print(msg)
        self.loop_flag = 0


    def on_reading(self, uid):
        self.nfc.stop_listening()
        msg = {
            'flag':'authentication',
            'card_uid': uid,
            'response_topic': f"{TOPIC_BASE}/validateAuthentication",
        }

        msg = json.dumps(msg)
        self.mqtt_client.loop_start()
        self.mqtt_client.subscribe(f"{TOPIC_BASE}/validateAuthentication")
        self.mqtt_client.publish(f"{TOPIC_BASE}/authentication", msg)

        self.loop_flag=1
        while self.loop_flag == 1:
            time.sleep(0.01)
        self.mqtt_client.loop_stop()
        self.mqtt_client.unsubscribe(f"{TOPIC_BASE}/validateAuthentication")
        self.nfc.listen(on_reading=self.on_reading)

my_authentication = RaspberryAuthentication()
