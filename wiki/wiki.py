import wikipedia
import simplejson as json

try:
	fo = open("../main/pipe.ali","r")
	wiki = json.load(fo)
	fo.close()
	print 'Wkik:',wiki['data']
	tmp = wikipedia.summary(wiki['data'],sentences=2)
	if '(' in tmp:
		tmp = str(tmp[:tmp.index('('):]+tmp[tmp.index(')')+2::])
	print wiki['bot'],':',tmp
	wiki = {
		'data':tmp
	}
	fo = open("../main/pipe.ali","w")
	json.dump(wiki,fo)
	fo.close()
except:
	print 'Sorry Couldnt Connect to internet now.'