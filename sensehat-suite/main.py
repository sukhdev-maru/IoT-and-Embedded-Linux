from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

# ---------------------------
# Temperature & Humidity
# ---------------------------
def temp_humidity():
    humidity = sense.get_humidity()
    temp = sense.get_temperature()
    print(f"Humidity: {humidity:.2f}%")
    print(f"Temperature: {temp:.2f} °C")


# ---------------------------
# Message Display
# ---------------------------
def show_message():
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    sense.show_message("Kirti P", text_colour=yellow, back_colour=blue)


# ---------------------------
# Smiley Display
# ---------------------------
def smiley():
    e = (255, 255, 255)
    k = (0, 0, 0)
    r = (255, 0, 0)

    image = [
        k,e,e,e,e,e,e,k,
        e,k,k,k,k,k,k,e,
        e,k,r,k,k,r,k,e,
        e,k,k,k,k,k,k,e,
        e,r,k,k,k,k,r,e,
        e,k,r,k,k,r,k,e,
        e,k,k,r,r,k,k,e,
        k,e,e,e,e,e,e,k
    ]

    sense.set_pixels(image)


# ---------------------------
# IMU Orientation
# ---------------------------
def imu_display():
    sense.show_letter("J")

    while True:
        acc = sense.get_accelerometer_raw()
        x = round(acc['x'], 0)
        y = round(acc['y'], 0)

        if x == -1:
            sense.set_rotation(180)
        elif y == 1:
            sense.set_rotation(90)
        elif y == -1:
            sense.set_rotation(270)
        else:
            sense.set_rotation(0)

        sleep(0.5)


# ---------------------------
# Joystick Mapping
# ---------------------------
sense.stick.direction_up = smiley
sense.stick.direction_down = imu_display
sense.stick.direction_left = show_message
sense.stick.direction_right = temp_humidity

while True:
    pass
