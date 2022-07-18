
import requests
import cv2 
import time 
import Jetson.GPIO as GPIO 
import os
from uuid import uuid4
from PIL import Image
import pathlib
import glob

pir_pin = 7
infrared = 13

homedir = os.environ['HOME']
image_path = homedir + '/images/'


GPIO.setmode(GPIO.BOARD) 

GPIO.setup(pir_pin, GPIO.IN)
GPIO.setup(infrared, GPIO.OUT)

GPIO.output(infrared, GPIO.HIGH) 

	
def gstreamer_pipeline(
	capture_width=640,
	capture_height=480,
	display_width=640,
	display_height=480,
	framerate=30,
	flip_method=2,
):
	 return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

def current_milli_time():
    return round(time.time() * 1000)


def get_timestamp(arg):
	t = time.localtime()
	if arg == 1:
		curr_time = time.strftime("%H-%M-%S-%Y-%m-%d",t)
		return curr_time
	if arg == 2:
		curr_time = time.strftime("%Y-%m-%d",t)
		return curr_time


def detect_motion():
	while GPIO.input(7) == 0:
		time.sleep(0.5)
	return 1
						
def detect_capture():

		GPIO.output(infrared, GPIO.LOW) 
		
		cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=2), cv2.CAP_GSTREAMER)	
		if cap.isOpened():
			
			
			x = uuid4().hex
			fixed_uuid = str(x)
			fixed_date = get_timestamp(1)
			
		

			if not os.path.exists(image_path + fixed_uuid ):
				os.makedirs(image_path + fixed_uuid )

							
			print("Starting capture")
			p = 0
			while p < 35: # to discard over exposure frames
				ret_val, img = cap.read()
				p = p + 1


			n=0
			while n < 15: # change for number of pictures
				ret_val, img = cap.read()
				mili = str(current_milli_time())
				loc = image_path + fixed_uuid + '/' + mili + '.jpg'
				cv2.imwrite(loc , img)
				
				n=n+1
				m = 0
				while m < 30:         # to discard next frames
					ret_val, img = cap.read()
					m = m + 1
	
			cap.release()
			print("done capturing")
			GPIO.output(infrared, GPIO.HIGH) 
		else:
			print("Unable to open camera")


if __name__ == "__main__":

	print("Initializing")	
	time.sleep(0.1)
	
	while True:

		print("started motion detect")
		detect_motion() 
		detect_capture()
		break
					
	GPIO.cleanup()
	time.sleep(3)
	
