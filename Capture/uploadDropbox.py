#!/usr/bin/python
import RPi.GPIO as GPIO
from subprocess import call
import time
import subprocess
import datetime
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)

def timestamp():
    tstring = datetime.datetime.now()
    return tstring.strftime("%Y-%m-%d-%H-%M-%S")

while True:
	input_state = GPIO.input(21)
	if input_state == True:
		filename = timestamp() + '5Code'
		path_file = "/Images/"
		print 'TERDETEKSI'
		#subprocess.call(['/home/pi/Documents/capture.sh'])
		os.system('fswebcam 320x240 -S 3 --jpeg 50 --save /home/pi/Documents/gambar/'+ filename +'.jpg')
		photofile = "/home/pi/Documents/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/Documents/gambar/"+ filename +".jpg "+path_file+""+filename +".jpg"   
		call ([photofile], shell=True)
 		time.sleep(10)



