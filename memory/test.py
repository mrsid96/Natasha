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

x = raw_input("Enter: ")
#print x,ch

print process.extractOne(x,ch)
#print process.extract(x,ch)
