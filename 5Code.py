from threading import Thread
import os
import subprocess
import mysql.connector
import time
import sys
import RPi.GPIO as GPIO

# -----------------------
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(15, GPIO.OUT)
# ----------------------

#Documents/5Code/Fingerprint/run.py


#def play_scriptA():
	#os.system("/home/pi/Documents/5Code/A.py")
	#subprocess.Popen(['/home/pi/Documents/5Code/A.py'], shell=True)

def play_scriptB():
	os.system("/home/pi/Documents/5Code/Fingerprint/run.py")

def play_scriptC():
	os.system("/home/pi/Documents/5Code/Capture/uploadDropbox.py")

def play_buzzerA():
        	GPIO.output(15, True)
        	time.sleep(0.5)
        	GPIO.output(15, False)
        	time.sleep(0.5)

def stop_buzzerA():
		GPIO.output(15, False)
		time.sleep(0.3)

def db_connect():
	    mydb = mysql.connector.connect(
      		host="192.168.43.195",
      		user="5code",
      		passwd="",
      		database="db_guardbox"
    	    )

   	    mycursor = mydb.cursor()
    	    mycursor.execute("SELECT * FROM tb_security")
            myresult = mycursor.fetchone()

	    global x

	    x = myresult
            print("Value state : ", x[1])
            print("Value sound : ", x[2])

            time.sleep(0.5)


global n

Thread(target = play_scriptB).start()
Thread(target = play_scriptC).start()

while True:
	try:
	    db_connect()
	#Thread(target = play_scriptB).start() 
	    while(x[2] == 1):
		print("Buzzer ON!");
		play_buzzerA()
		break

	    while(x[2] == 0):
		print("Buzzer Off!");
		stop_buzzerA()
		break

	except KeyboardInterrupt:
	    
            GPIO.cleanup()
	    sys.exit()
