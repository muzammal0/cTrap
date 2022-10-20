# GPIO library
import Jetson.GPIO as GPIO
 
# Handles time
import time 
 
# Pin Definition
led_pin = 36
 
# Set up the GPIO channel
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW) 
 
print("Press CTRL+C when you want the LED to stop blinking") 
 
# Blink the LED
while True: 
   
  GPIO.output(led_pin, GPIO.HIGH) 
  print("usb is OFF")
  time.sleep(10) 
  GPIO.output(led_pin, GPIO.LOW)
  print("usb is On")
  time.sleep(10)
