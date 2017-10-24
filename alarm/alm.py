import threading
import time
from datetime import datetime
import datetime as dt

def alarm():
    a,b = input("Hour & Minutes : ")
    req_time = str(dt.time(a,b,0))
    req_time = req_time[:5]
    while 1:
	    current_time = str(datetime.now().time())
	    current_time = current_time[:5]
	    if(req_time == current_time):
            	print ("There is a alarm")
            	break

#Create a new alarm instance
def create_alarm():
	t = threading.Thread(target = alarm)
	t.start()

create_alarm()
create_alarm()
	