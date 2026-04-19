import time
import telepot
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO

LED_PIN = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)


def led_on():
    GPIO.output(LED_PIN, GPIO.HIGH)


def led_off():
    GPIO.output(LED_PIN, GPIO.LOW)


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg.get('text', '').lower()

    print("Command:", command)

    if command == "on":
        led_on()
        bot.sendMessage(chat_id, "LED ON")

    elif command == "off":
        led_off()
        bot.sendMessage(chat_id, "LED OFF")


bot = telepot.Bot("YOUR_BOT_TOKEN")

MessageLoop(bot, handle).run_as_thread()

print("Bot is running...")

while True:
    time.sleep(10)
