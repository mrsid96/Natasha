import pyowm
import simplejson as json

owm = pyowm.OWM('532d313d6a9ec4ea93eb89696983e369')
try:
	fo = open("../main/pipe.ali","r")
	wea = json.load(fo)
	fo.close()
	print wea['place'],'Weather Information'
	observation = owm.weather_at_place(wea['place'])  
	w = observation.get_weather()  
	temperature = w.get_temperature('celsius')  
	tomorrow = pyowm.timeutils.tomorrow()  
	wind = w.get_wind()  
	detailed = w.get_detailed_status().lower()
	if (detailed == 'clear sky'):
		detailed = 'Khula akash'
	elif (detailed == 'few clouds'):
		detailed = 'Akash main kam badal'
	elif (detailed == 'scattered clouds'):
		detailed = 'Akash main bikhra hua badal'
	elif (detailed == 'broken clouds'):
		detailed = 'Akash main bikhra hua badal'
	else:
		detailed = w.get_detailed_status().lower()
	print wea['bot']+' : '+detailed +' aur hawa ki gati '+str(wind['speed'])+', aur taapamatra '+str(temperature['temp'])+' celsius aur humidity '+str(w.get_humidity())+'%'
	wea = {
			'data':detailed +' aur hawa ki gati '+str(wind['speed'])+', aur taapamatra '+str(temperature['temp'])+' celsius aur humidity '+str(w.get_humidity())+'%'
			}
	fo = open("../main/pipe.ali","w")
	json.dump(wea,fo)
	fo.close()
except:
	print 'Sorry couldnt connect to internet'