import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)
while  True:
	input_state = GPIO.input(21)
	if input_state == True:
		print 'TERDETEKSI'
		subprocess.call(['/home/pi/Documents/capture.sh'])
		time.sleep(2)
		
