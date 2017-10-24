import requests
import simplejson as json

try:
	fo = open("../main/pipe.ali","r")
	swi = json.load(fo)
	fo.close()
	print 'Turning',swi['status'],swi['number'],swi['device']
	load=""
	st=""
	#routing the commands
	if(swi['device']=='fan'):
		if(swi['number']=='first' or swi['number']=='1st'):
			load='FOne'
		elif(swi['number']=='second' or swi['number']=='2nd'):
			load='FTwo'
		else:
			load='FThree'

		if(swi['status']=='on'):
			st='O'
		else:
			st='F'	
	else:
		if(swi['number']=='first' or swi['number']=='1st'):
			load='LOne'
		else:
			load='LTwo'
			
		if(swi['status']=='on'):
			st='O'
		else:
			st='F'

	res = requests.get('http://172.17.2.6/aisha/index.php?sid='+load+'&status='+st)
	if(res.status_code == 200):
		wea = {
			'data':'Done Sir'
			}
		fo = open("../main/pipe.ali","w")
		json.dump(wea,fo)
		fo.close()
	else:
		wea = {
			'data':'i\'m Unable to reach the network, sir.'
			}
		fo = open("../main/pipe.ali","w")
		json.dump(wea,fo)
		fo.close()
except:
	print 'Sorry'
