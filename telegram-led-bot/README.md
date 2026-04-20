# Telegram LED Control Bot

## Overview

This project enables remote control of a Raspberry Pi GPIO pin using a Telegram bot. Users can send commands via chat to toggle an LED.

---

## Features

* Remote LED control via Telegram
* Simple command-based interface
* Real-time response

---

## Technologies Used

* Python 3
* telepot
* RPi.GPIO

---

## Hardware Requirements

* Raspberry Pi
* LED
* 220Ω resistor

---

## Wiring

* Pin 11 → Resistor → LED → GND

---

## Setup

### 1. Create Telegram Bot

* Use BotFather in Telegram
* Generate bot token

### 2. Update Code

Replace:

```
YOUR_BOT_TOKEN
```

with your actual token

---

## Installation

```bash
pip install telepot
```

---

## How to Run

```bash
python3 telegram_bot.py
```

---

## Commands

| Command | Action       |
| ------- | ------------ |
| on      | Turn LED ON  |
| off     | Turn LED OFF |

---

## Expected Output

* LED turns ON/OFF based on Telegram commands
* Console prints received commands

---

## Security Note

* Never expose your bot token publicly
* Use environment variables for production

---

## Future Improvements

* Add multiple device control
* Add authentication
* Integrate with IoT dashboard
