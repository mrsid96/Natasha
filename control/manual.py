#Raspberry Pi GPIO
import RPi.GPIO as GPIO
from time import sleep

#Init the GPIO Mode
GPIO.setmode(GPIO.BCM)

#Setting up the pins
GPIO.setup(17,GPIO.OUT)

while 1:
	GPIO.output(17,GPIO.HIGH)
	sleep(1)
	GPIO.output(17,GPIO.LOW)
	sleep(1)