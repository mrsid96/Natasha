import os
import time
from multiprocessing import Process
import random

def greetings()	:
	
def news():
	time.sleep(random.randint(1, 3))
    os.system("python ../news/news.py")
def notifications():
	time.sleep(random.randint(1, 3))
    os.system("python ../notifications/gmail_noti.py")
def weather():
	time.sleep(random.randint(1, 3))
    os.system("python ../weather/wea.py")
def events():
	time.sleep(random.randint(1, 3))
    os.system("python ../remAlert/event.py")


greetings()
news()
notifications()
weather()
events()