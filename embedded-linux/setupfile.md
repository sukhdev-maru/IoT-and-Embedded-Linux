# Setup Notes – Embedded Linux (Raspberry Pi)

## Environment

* Device: Raspberry Pi (Model 5)
* OS: Raspberry Pi OS (Debian-based)
* Interface: Terminal (CLI) + Thonny IDE

---

## 1. System Update

Before installing packages:

```bash
sudo apt-get update
sudo apt-get upgrade
```

---

## 2. GPIO Setup

### Attempt (Incorrect Command)

```bash
sudo apt-get Rpi.GPIO
```

### Issue

* Invalid command syntax

### Correct Installation

```bash
sudo apt-get install python3-rpi.gpio
```

### Observation

* `RPi.GPIO` shows compatibility issues on Raspberry Pi 5
* Recommended alternative:

```bash
pip install gpiozero
```

---

## 3. Python Package Installation

### MQTT & GPIO

```bash
pip install paho-mqtt gpiozero
```

### Telegram Bot

```bash
pip install telepot
```

### Note

* Warning about system-managed Python packages
* Use `--break-system-packages` only if required

---

## 4. Network Configuration

### Access Configuration File

```bash
cat /etc/dhcpcd.conf
```

### Attempt to Edit

```bash
vim dhcpcd.conf
```

### Issue

* `vim` not installed

### Alternative

```bash
nano dhcpcd.conf
```

---

## 5. Common Errors Observed

### 1. Invalid Command

```text
E: Invalid operation Rpi.GPIO
```

**Cause:** Wrong apt syntax
**Fix:** Use `apt-get install`

---

### 2. Command Not Found

```text
bash: vim: command not found
```

**Fix:**

```bash
sudo apt-get install vim
```

---

### 3. Package Conflicts

* Mixing `apt` and `pip` installs
* Some packages already managed by system

---

## 6. Best Practices Learned

* Always run `apt-get update` before installing
* Prefer `gpiozero` over `RPi.GPIO` on Pi 5
* Avoid mixing `pip` and `apt` unnecessarily
* Use `nano` if `vim` is not available
* Read error messages carefully—they are usually explicit

---

## 7. Verification

### Check Installed Packages

```bash
pip list
```

### Check GPIO Functionality

* Run simple LED blink test
* Verify physical connections

---

## 8. Summary

This setup process involved:

* Installing required libraries
* Handling compatibility issues
* Debugging command errors
* Understanding Linux package management

The system is now ready for:

* MQTT-based IoT applications
* Telegram bot integration
* GPIO-based hardware control
