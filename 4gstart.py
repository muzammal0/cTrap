
# GPIO library
import Jetson.GPIO as GPIO

# Handles time
import time

# Pin Definition
usb_pin = 36

# Set up the GPIO channel
GPIO.setmode(GPIO.BOARD)
GPIO.setup(usb_pin, GPIO.OUT, initial=GPIO.LOW)
time.sleep(2)
GPIO.output(usb_pin, GPIO.LOW)
print("usb is On")
time.sleep(10)

