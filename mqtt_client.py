import paho.mqtt.client as mqtt

BROKER = 'localhost'
PORT = 1883



class ScoreMQTTClient:
    def __init__(self, topic='pinball/score'):
        self.client = mqtt.Client()
        self.topic = topic
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(BROKER, PORT, 60)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print(f"[ScoreMQTT] Connected with MQTT Broker (code {rc})")

    def on_message(self, client, userdata, msg):
        print(f"[ScoreMQTT] Received: {msg.payload.decode()}")


    def send_score(self, score):
        message = f"Score: {score}"
        self.client.publish(self.topic, message)
        print(f"[ScoreMQTT] Sent score: {score}")

class GameMQTTClient:
    def __init__(self, topic='pinball/game'):
        self.client = mqtt.Client()
        self.topic = topic
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(BROKER, PORT, 60)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print(f"[GameMQTT] Connected with MQTT Broker (code {rc})")

    def on_message(self, client, userdata, msg):
        print(f"[GameMQTT] Received: {msg.payload.decode()}")


    def send_hit(self, hit_type):
        message = f"Score: {hit_type}"
        self.client.publish(self.topic, message)
        print(f"[ScoreMQTT] Sent score: {hit_type}")
