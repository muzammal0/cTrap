# GPIO library
import Jetson.GPIO as GPIO
 
# Handles time
import time
 
# Pin Definition
sen1 = 11
sen2 = 13
 
# Set up the GPIO channel
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sen1, GPIO.IN)
GPIO.setup(sen2, GPIO.IN)
 
print("Press CTRL+C when you want the LED to stop blinking")
# Blink the LED
while True:
	m1 = GPIO.input(sen1)
	m2 = GPIO.input(sen2)
	if m1 == 1 & m2 == 1:
		print("Both Trigered")
	elif m2 == 1:
		print("2nd Trigered")
	elif m1 == 1:
		print("1st Trigerred")
	else:
		print("null")
	t = time.localtime()
	curr_time = time.strftime("%H-%M-%S-%Y-%m-%d",t)
	print(curr_time)
	time.sleep(1)
GPIO.cleanup()
  
