# Sense HAT Interactive Suite

## Overview

This project implements an interactive application using the Raspberry Pi Sense HAT. It allows users to access sensor data, display visuals, and control outputs using the onboard joystick.

---

## Features

* Temperature and humidity monitoring
* LED matrix smiley display
* Scrolling text display
* IMU-based orientation detection
* Joystick-based control system

---

## Technologies Used

* Python 3
* Sense HAT library

---

## Controls

| Direction | Function               |
| --------- | ---------------------- |
| Up        | Display Smiley         |
| Down      | IMU Orientation        |
| Left      | Show Message           |
| Right     | Temperature & Humidity |

---

## Installation

```bash
sudo apt install sense-hat
pip install sense-hat
```

---

## How to Run

```bash
python3 main.py
```

---

## Expected Output

* Terminal displays temperature and humidity values
* LED matrix shows smiley or scrolling message
* Display rotates based on device orientation

---

## Notes

* Ensure Sense HAT is properly connected
* Run with appropriate permissions if required

---

## Future Improvements

* Add data logging
* Integrate with cloud dashboard
* Add gesture-based controls
