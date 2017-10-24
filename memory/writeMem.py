#Write Mem
import simplejson as json

fo = open("mem.ali",'r')
data = json.load(fo)
fo.close()

data["data"+str(len(data)+1)]=raw_input("Enter Mem here: ")

fo = open("mem.ali",'w')
json.dump(data,fo)
fo.close()