#!/usr/bin/python
import os

try:
	i = 0
	while True:
    	#os.pause(10)
    		os.system("/home/pi/Documents/5Code/Fingerprint/ReadF.py")
    		time.sleep(5)
		

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
