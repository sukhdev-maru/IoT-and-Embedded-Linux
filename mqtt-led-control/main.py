from gpiozero import LED
import paho.mqtt.client as mqtt

LED_PIN = 17
led = LED(LED_PIN)

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "test/switch123"


def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected:", reason_code)
    client.subscribe(TOPIC)


def on_message(client, userdata, msg):
    payload = msg.payload.decode().strip()
    print("Received:", repr(payload))

    if payload == "1":
        led.on()
    elif payload == "0":
        led.off()


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()
