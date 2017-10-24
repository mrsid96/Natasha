#Remember Module
import simplejson as json

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

fo = open("../memory/mem.ali",'r')
data = json.load(fo)
fo.close()

ch=[]

for i in data:
	ch.append(data[i])

fo = open("../main/pipe.ali",'r')
que = json.load(fo)
fo.close()

x = que['query']
print x,ch
x = process.extractOne(x,ch)[0]
pipe = {
		'data':x
		}
fo = open("../main/pipe.ali","w")
json.dump(pipe,fo)
fo.close()