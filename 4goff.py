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
print("usb is off")
GPIO.output(usb_pin, GPIO.HIGH) #off
time.sleep(10)
