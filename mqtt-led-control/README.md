# MQTT LED Control (Raspberry Pi 5)

## Overview

This project demonstrates remote control of a physical LED connected to a Raspberry Pi using the MQTT protocol. A client (mobile app or web dashboard) publishes messages to a broker, and the Raspberry Pi subscribes to the topic and toggles the LED accordingly.

---

## Architecture

```
Publisher (Phone / PC)
        ↓
   MQTT Broker (HiveMQ)
        ↓
 Raspberry Pi (Subscriber)
        ↓
      LED (GPIO17)
```

---

## Features

* Real-time LED control via MQTT
* Lightweight and low-latency communication
* Compatible with mobile apps (IoT MQTT Panel)
* Works with public brokers (HiveMQ)

---

## Technologies Used

* Python 3
* MQTT (paho-mqtt)
* Raspberry Pi GPIO (gpiozero)
* HiveMQ public broker

---

## Hardware Requirements

* Raspberry Pi 5
* LED
* 220Ω–330Ω resistor
* Breadboard + jumper wires

---

## Wiring

* GPIO17 (Pin 11) → Resistor → LED (anode)
* LED cathode → GND (Pin 6)

---

## MQTT Configuration

* Broker: `broker.hivemq.com`
* Port: `1883`
* Topic: `test/switch123`

### Payload Mapping

| Payload | Action  |
| ------- | ------- |
| `1`     | LED ON  |
| `0`     | LED OFF |

---

## Installation

Install required libraries:

```bash
pip install paho-mqtt gpiozero
```

---

## Running the Project

```bash
python3 mqtt_led.py
```

Expected output:

```
Connected: 0
Received: '1'
```

---

## Testing

You can publish messages using:

* Mobile app: IoT MQTT Panel
* Web client: HiveMQ WebSocket Client

Publish to:

```
test/switch123
```

---

## Troubleshooting

### LED not turning ON/OFF

* Verify wiring (GPIO17 → Pin 11)
* Check resistor and LED polarity

### No messages received

* Ensure topic matches exactly
* Confirm broker and port are correct
* Check internet connectivity

### SSL Errors

* Use port `1883` (no TLS)
* Do not enable `tls_set()` unless using port `8883`

---

## Future Improvements

* Add sensor feedback (temperature, humidity)
* Implement secure MQTT (TLS + authentication)
* Integrate with cloud dashboard
* Add relay module for real-world devices

---

## Author

SK

---

## License

MIT License
