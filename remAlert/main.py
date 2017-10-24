import time
from datetime import datetime
import datetime 
from multiprocessing import Process
import os
import random

def event():
    time.sleep(random.randint(1, 3))
    os.system("python event.py")

def reminder():
    time.sleep(random.randint(1, 3))
    os.system("python remind.py")

def manage(eve,rem):
    if (eve == 1 and rem ==1):
    	p1.start()
    	p2.start()
    	processes.append(p1)
	processes.append(p2)
    elif (eve == 1):
    	p1.start()
    	processes.append(p1)
    elif (rem == 1):
    	p2.start()
    	processes.append(p2)
    
processes = []
p1 = Process(target=event)
p2 = Process(target=reminder)

eve = input()
rem = input()
manage(eve,rem)

for p in processes:
       p.join()



