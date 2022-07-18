
# GPIO library
import Jetson.GPIO as GPIO
import os
# Handles time
import time 
import getpass
import os.path
import socket
 
# Pin Definition
led_pin = 16
gnd_pin = 18

 
# Set up the GPIO channel
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(gnd_pin, GPIO.OUT) 
GPIO.setwarnings(False) 

username = getpass.getuser()
homedir = os.environ['HOME']
hostname = socket.gethostname()
print(username)
print(homedir) 
print(hostname) 
 
# Blink the LED
while True: 
  print('filter is HIGH')
  GPIO.output(led_pin, GPIO.LOW)
  GPIO.output(gnd_pin, GPIO.HIGH) 
  time.sleep(2)
  print('filter is LOW NIGHTVISION ON')
  GPIO.output(gnd_pin, GPIO.LOW)
  GPIO.output(led_pin, GPIO.HIGH)
  time.sleep(2) 
  
  GPIO.setwarnings(False) 
