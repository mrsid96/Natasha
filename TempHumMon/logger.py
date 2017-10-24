#monitor the temp and humidity

import RPi.GPIO as GPIO
import dht11
import requests
import calendar
import time
from datetime import date

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

while 1:
		time.sleep(30)
		# read data using pin 14
		instance = dht11.DHT11(pin = 4)
		result = instance.read()

		#getting current day of week
		my_date = date.today()
		day=calendar.day_name[my_date.weekday()]

		tmpstp = time.strftime("%H:%M")

		if result.is_valid():
			print("Temperature: %d C" % result.temperature)
			print("Humidity: %d %%" % result.humidity)
			res = requests.get('http://trashit.hol.es/room/?day='+day+'&time='+tmpstp+'&temp='+str(result.temperature)+'&hum='+str(result.humidity))
		else:
			print("Error: %d" % result.error_code)
