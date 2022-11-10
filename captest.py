
import requests
import cv2 
import time 
import Jetson.GPIO as GPIO 
import os
from uuid import uuid4
from PIL import Image
import pathlib
import glob
import os
	
def gstreamer_pipeline(
	capture_width=640,
	capture_height=480,
	display_width=640,
	display_height=480,
	framerate=30,
	flip_method=0,
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


						
def detect_capture():

		 
		user = os.getlogin()
		print(user)
		cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)	
		if cap.isOpened():
			
			
			x = uuid4().hex
			fixed_uuid = str(x)
			fixed_date = get_timestamp(2)
			
		

			if not os.path.exists('/home/'+str(user)+'/images'):
				os.makedirs('/home/'+str(user)+'/images')

							
			print("Starting capture")
			p = 0
			while p < 20: # to discard over exposure frames
				ret_val, img = cap.read()
				p = p + 1

			n=0
			while n < 3:
				ret_val, img = cap.read()
				mili = str(current_milli_time())
				loc = '/home/'+str(user)+'/images' + mili + '.jpg'
				cv2.imwrite(loc , img)
				
				n=n+1
				m = 0
				while m < 30:         # to discard next frames
					ret_val, img = cap.read()
					m = m + 1
	
			cap.release()
			print("done capturing")
			 
		else:
			print("Unable to open camera")


if __name__ == "__main__":

	print("Initializing")	
	time.sleep(0.1)
	

	detect_capture()
					
	