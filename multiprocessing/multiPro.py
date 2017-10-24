import time
from datetime import datetime
import datetime 
from multiprocessing import Process
import os
import random

def recieve_sensor():
    time.sleep(random.randint(1, 3))
    os.system("python event.py")

def sound_record():
    time.sleep(random.randint(1, 3))
    os.system("python remind.py")

def reminder_alert():
    time.sleep(random.randint(1, 3))
    os.system("python ../remAlert/main.py")

def notification():
    time.sleep(random.randint(1, 3))
    os.system("python ../notification/gmail_noti.py")

processes = []
p1 = Process(target=recieve_sensor)
p2 = Process(target=sound_record)
p3 = Process(target=reminder_alert)
p4 = Process(target=notification)

p1.start()
p2.start()
p3.start()
p4.start()

for p in processes:
       p.join()



