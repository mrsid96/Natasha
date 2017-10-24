import time
from datetime import datetime
import datetime as dt
import _thread
import time

def main(summary):
    a = input("Hour : ")
    b = input("Minutes : ") 
    req_time = str(dt.time(a,b,0))
    req_time = req_time[:5]
    while 1:
	    current_time = str(datetime.now().time())
	    current_time = current_time[:5]
	    if(req_time == current_time):
            	print ("There is a reminder")
            	break
		      	
count =0
# Create new alarm
def new_alarm(): 
    try:
        count += 1
        _thread.start_new_thread( main, ("Alarm-"+count, ) )
    except:
       print ("Error: unable to set alarm")

    while 1:
       pass

main("")
