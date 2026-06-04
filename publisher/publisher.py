import time
import json
import random
import paho.mqtt.client as mqtt

BROKER = "mosquitto"
PORT = 1883
TOPIC = "labcontrol/machines/metrics"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

while True:
    payload = {
        "machineId": str(random.randint(1,5)),
        "temperature": round(20 + random.random() * 10,2),
        "vibration": round(random.random() * 5,2),
        "timestamp": int(time.time())
    }
    client.publish(TOPIC, json.dumps(payload))
    print(f"Published: {payload}")
    time.sleep(2)
