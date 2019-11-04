import paho.mqtt.client as mqtt
import json

from public.config import BROKER_PWD, BROKER_USR, HOST, TOPIC_BASE, SCRIPT_DB, DB_NAME
from components.message_manager import MessageManager
from components.db import Database

def action(data):
    # verifs ici ?
    if data['flag'] == "authentication":
        results = db.select(table='users', conditions=[("card_uid", data["card_uid"])])
        if len(results) > 0 :
            data['authorization'] = "granted"
            data['last_name'] = results[0]["last_name"]
            data['first_name'] = results[0]["first_name"]
        else:
            data['authorization'] = "failed"

    return data

def on_message(client, userdata, message):
    #decode message to have a dict
    msg = message.payload.decode('utf-8')
    msg = json.loads(msg)
    msg['action'] = action

    MessageManager(client, msg)
server = mqtt.Client('server')
db = Database(db_name=DB_NAME, db_script=SCRIPT_DB)

# server.on_message = on_message
# server.username_pw_set(username=BROKER_USR, password=BROKER_PWD)
# server.connect(HOST)
# server.subscribe(f"{TOPIC_BASE}/authentication")
# server.loop_forever()


# tuples = (
#     ('85AF54', 'Bocquet', 'Anthony'),
#     ('GLJG54', 'Ouakrim', 'Yanis'),
# )
#db.insert('users', tuples, many=True);

print(db.select('users' , many=True))
db.update('users', [('last_name', 'richard'), ('first_name', 'quentin')], conditions=[('last_name', 'quentin'), ('first_name', 'richard')])

print(db.select('users', many=True))
