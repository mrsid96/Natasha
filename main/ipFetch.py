import os
from subprocess import Popen,PIPE
#Getting the network hosted IP
devs = os.listdir('/sys/class/net/')
for i in devs:
	if (i[0]=='w' and i[1]=='l'):
		devs = i
		break
devs = "ip -4 addr show "+devs+" | grep inet | awk '{print $2}' | cut -d/ -f1"
proc = Popen(devs, shell=True, stdout=PIPE, stderr=PIPE)
ipNet = proc.communicate()[0]
ipNet = str(''.join(ipNet.split()))
print ipNet