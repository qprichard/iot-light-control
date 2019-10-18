from classes.mqtt import MQTT
from classes.nfc_reader import NFCReader
from public.config import BROKER_PWD, BROKER_USR, SERVER_URL, TOPIC_BASE


nfc = NFCReader()

my_mqtt = MQTT()
my_mqtt.usr_pw_set(username=BROKER_USR, password=BROKER_PWD)
my_mqtt.connect(SERVER_URL)

def on_reading(data):
    my_mqtt.publish(f"{TOPIC_BASE}/authentication", data)

nfc.listen(on_reading=on_reading)
