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
	print wea['bot']+' : '+w.get_detailed_status() +' with wind speed '+str(wind['speed'])+', temperature is '+str(temperature['temp'])+' celsius and humidity is '+str(w.get_humidity())+'%'
	wea = {
			'data':w.get_detailed_status() +' with wind speed '+str(wind['speed'])+', temperature is '+str(temperature['temp'])+' celsius and humidity is '+str(w.get_humidity())+'%'
			}
	fo = open("../main/pipe.ali","w")
	json.dump(wea,fo)
	fo.close()
except:
	print 'Sorry couldnt connect to internet'