import paho.mqtt.client as mqtt

BROKER = 'localhost'
PORT = 1883
TOPIC = 'pinball/score'

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code" + str(rc))

def on_message(client, userdata, msg):
    print(f"Message received {msg.payload.decode()}")

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

client.loop_start()

def send_score(score):
    message = f"Score: {score}"
    client.publish(TOPIC, message)
    print(f"Sent score: {score} to topic {TOPIC}")


