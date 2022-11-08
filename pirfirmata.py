# GPIO library
import Jetson.GPIO as GPIO
import pyfirmata
 
# Handles time
import time
 
# Pin Definition
sen1 = 11
sen2 = 13
 
# Set up the GPIO channel
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sen1, GPIO.IN)
GPIO.setup(sen2, GPIO.IN)
try:
	board = pyfirmata.Arduino('/dev/ttyUSB0')
	print("Communication Successfully started")

	while True:

		m1 = GPIO.input(sen1)
       		m2 = GPIO.input(sen2)
		if m1 == 1 & m2 == 1:
			board.digital[4].write(1)
			board.digital[2].write(1)
			print("Both Trigered")
		elif m2 == 1:
			print("2nd Trigered")
			board.digital[4].write(1)
			board.digital[2].write(0)
		elif m1 == 1:
			print("1st Trigerred")
			board.digital[2].write(1)
			board.digital[4].write(0)
		else:
			print("null")
			board.digital[2].write(0)
			board.digital[4].write(0)
		t = time.localtime()
		curr_time = time.strftime("%H-%M-%S-%Y-%m-%d",t)
		print(curr_time)
		time.sleep(.1)
		

except:
		print("Arduino not found")
		time.sleep(1)
  		

