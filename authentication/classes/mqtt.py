import paho.mqtt.client as mqtt
from public.config import BROKER_PWD, BROKER_USR, SERVER_URL

class MQTT():
    def __init__(
        self,
        on_connect = None,
        on_message = None,
        client_id = None,
        clean_session = True,
        user_data = None,
        transport = "tcp"
    ):
        self.client = mqtt.Client(
            client_id = client_id,
            clean_session = clean_session,
            userdata = user_data,
            transport = transport
            )

        self.client.on_connect = on_connect
        self.client.on_message = on_message


    def reinitialise(self, client_id = None, clean_session = True, user_data = None):
        """
        Reinitialise method
        """
        self.client.reinitialise(client_id=client_id, clean_session=clean_session, userdata=user_data)

    def enable_logger(self, logger=None):
        """
        Enable the logger
        """
        self.client.enable_logger(logger=logger)

    def disable_logger(self):
        """
        Disable the logger
        """
        self.client.disable_logger()

    def usr_pw_set(self, username, password=None):
        """
        Set username and a password for broker authentication
        must be called before connect()
        """
        self.client.username_pw_set(username=username, password=password)

    def user_data_set(self, data):
        """
        Set the user data
        """
        self.client.user_data_set(data)

    def connect(self, host, port=1883, keepalive=60, bind_address=""):
        self.client.connect(host, port, keepalive, bind_address)

    def publish(self, topic, payload=None, qos=0, retain=False):
        self.client.publish(topic, payload, qos, retain)

    def subscribe(self, topic):
        """
        (topic, qos)
        [(topic, qos), (topic,qos)]
        """
        self.client.subscribe(topic)

    def unsubscribe(self, topic):
        self.client.unsubscribe(topic)
