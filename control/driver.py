#Raspberry Pi GPIO
import RPi.GPIO as GPIO
import MySQLdb
from time import sleep

#Init the GPIO Mode
GPIO.setmode(GPIO.BCM)

#Setting up the pins
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

#Infinite Loop.
while 1:
	db = MySQLdb.connect("localhost","root","Sidharth12","natasha")
	cur = db.cursor()
	cur.execute("select * from switches")
	data = list(cur.fetchone())
	db.close()

	#changing the switches
	#For light 1
	if(data[0]=='ON'):
		GPIO.output(17,GPIO.HIGH)
	else:
		GPIO.output(17,GPIO.LOW)
	#For fan 1
	if(data[1]=='ON'):
		GPIO.output(18,GPIO.HIGH)
	else:
		GPIO.output(18,GPIO.LOW)
	#For 
	if(data[2]=='ON'):
		GPIO.output(27,GPIO.HIGH)
	else:
		GPIO.output(27,GPIO.LOW)
	#For 
	if(data[3]=='ON'):
		GPIO.output(22,GPIO.HIGH)
	else:
		GPIO.output(22,GPIO.LOW)
	#For 
	if(data[4]=='ON'):
		GPIO.output(23,GPIO.HIGH)
	else:
		GPIO.output(23,GPIO.LOW)
	sleep(2)
