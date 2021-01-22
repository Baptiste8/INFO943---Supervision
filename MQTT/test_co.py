# -*- coding: utf-8 -*-



import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata,flags , rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("info_docker")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode(encoding='UTF-8')))

client = mqtt.Client("FI_5_recherche_un_stage")

client.on_connect = on_connect
client.on_message = on_message
#client.username_pw_set(username="try", password="try")
client.connect("192.168.1.6", 1883, 60)

client.loop_start()
a=""
while a!="true":

    a=input(">")
    client.publish("commance", payload=a)


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_stop()
