#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.

"""

import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.OUT)

p = GPIO.PWM(18,50)
p.start(7.5)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buzzer = 15
GPIO.setup(buzzer,GPIO.OUT)


## Search for a finger
##

## Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    GPIO.cleanup()
    exit(1)

## Gets some sensor information
print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

## Tries to search the finger and calculate hash
try:
    print('Waiting for finger...')

    ## Wait that finger is read
    while ( f.readImage() == False ):
        pass

    ## Converts read image to characteristics and stores it in charbuffer 1
    f.convertImage(0x01)

    ## Searchs template
    result = f.searchTemplate()

    positionNumber = result[0]
    accuracyScore = result[1]

    if ( positionNumber == -1 ):
	while (positionNumber == -1):
        	print('No match found!')
        	#####################
        	GPIO.output(buzzer,GPIO.HIGH)
        	print ("Beep")
        	time.sleep(0.5) # Delay in seconds
        	GPIO.output(buzzer,GPIO.LOW)
        	print ("No Beep")
        	time.sleep(0.5)
	#IF positionNumber TRUE

    else:
       # print('Found template at position #' + str(positionNumber))
       # print('The accuracy score is: ' + str(accuracyScore))
	GPIO.output(buzzer, GPIO.LOW)

	try:
		while True:
			GPIO.output(buzzer, GPIO.LOW)
			p.ChangeDutyCycle(12.5)
			time.sleep(1)
			p.ChangeDutyCycle(2.5)
			time.sleep(3)
			p.stop()
			GPIO.cleanup()
			exit()

	except KeyboardInterrupt:
		p.stop()
		GPIO.cleanup()

    ## OPTIONAL stuff
    ##

    ## Loads the found template to charbuffer 1
    f.loadTemplate(positionNumber, 0x01)

    ## Downloads the characteristics of template loaded in charbuffer 1
    #characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')

    ## Hashes characteristics of template
    #print('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())

except KeyboardInterrupt:
                GPIO.output(buzzer, GPIO.LOW)
                GPIO.cleanup()
		exit()


except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    GPIO.cleanup()
    exit(1)
