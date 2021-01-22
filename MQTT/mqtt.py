import docker
import time
import json
import paho.mqtt.client as mqtt

def on_connect(client,userdata,flag,rc):
	print("connect with : "+str(rc))
	
	client.subscribe("commande")
	
def on_message(client,userdata,msg):
	print(msg.topic+" "+str(msg.payload.decode(encoding='UTF-8')))
	
client = mqtt.Client("mqtt_docker")
client.on_connect=on_connect
client.on_message=on_message
client.connect("127.0.0.1",1883,60)
client_docker = docker.from_env()





while True:

	time.sleep(10)
	for container in client_docker.containers.list():
		for j in container.stats():
			client.publish("info_docker",payload=j)
		

#while True:
#	for container in client.containers.list():
#		print(container.logs())
#		for j in container.stats():
#		
#			print(json.loads(j)['cpu_stats'])
#			
#		time.sleep(4)
