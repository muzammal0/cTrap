
#import RPi.GPIO as GPIO # Import the GPIO library.
import Jetson.GPIO as GPIO
import time # Import time library
GPIO.setmode(GPIO.BOARD)

GPIO.setup(33, GPIO.OUT)
pwm=GPIO.PWM(33, 100)
dc=0 # set dc variable to 0 for 0%
pwm.start(dc)
pwm.ChangeDutyCycle(80)
time.sleep(20)
pwm.ChangeDutyCycle(0)
time.sleep(2)
