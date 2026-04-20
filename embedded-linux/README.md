# Embedded Linux Practice (Raspberry Pi)

## Overview

This folder contains basic Embedded Linux operations and commands performed on a Raspberry Pi environment. It demonstrates familiarity with system configuration, package management, and low-level interaction with the Linux OS.

---

## Objectives

* Understand Linux system configuration
* Work with package management (APT, pip)
* Explore GPIO setup and dependencies
* Practice terminal-based development workflow

---

## Topics Covered

* GPIO library installation (`RPi.GPIO`, `gpiozero`)
* Package management using `apt-get` and `pip`
* System configuration files (`dhcpcd.conf`)
* Python environment setup
* Troubleshooting Linux commands

---

## Key Commands Used

### Package Installation

```bash
sudo apt-get update
sudo apt-get install python3-rpi.gpio
pip install telepot
pip install paho-mqtt gpiozero
```

---

### File Handling & Configuration

```bash
cat dhcpcd.conf
sudo nano dhcpcd.conf
```

---

### Debugging & Errors

* Handling invalid commands
* Resolving missing packages
* Understanding permission issues

---

## Observations

* Some libraries (e.g., `RPi.GPIO`) show compatibility issues on newer Raspberry Pi models (Pi 5)
* `gpiozero` is preferred for modern GPIO handling
* Proper use of package managers is critical to avoid conflicts

---

## Screenshots / Logs

(Add images here if needed)

---

## Learning Outcomes

* Improved understanding of Embedded Linux environment
* Hands-on experience with Raspberry Pi system configuration
* Ability to troubleshoot installation and runtime issues

---

## Future Work

* Shell scripting automation
* System service management (systemd)
* Device driver basics
* Network configuration

---

## Notes

This is a practice-oriented module and complements the IoT projects in this repository.
