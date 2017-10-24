import cv2, sys, numpy, os
import urllib,requests, simplejson as json

haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'datasets'  #All the faces data will be present this folder
(width, height) = (130, 100)
face_cascade = cv2.CascadeClassifier(haar_file)

url='http://192.168.0.14/server/?listusers'
r = requests.get(url);

users=[]

for i in range(len(r.json())):
	users.append(str(r.json()[i]['user']))

for i in users:
	url='http://192.168.0.14/count.php?user='+i
	res = requests.get(url).json()
	if(res['check']=='True'):
		print 'Importing '+i+', please wait...'
		count = res['nos']+1
		if not os.path.exists('orgImg/'+i):
		    os.makedirs('orgImg/'+i)
		for j in range(1,count):
			urllib.urlretrieve("http://192.168.0.14/images/"+i+"/"+str(j)+".jpg", "orgImg/"+i+"/"+str(j)+".jpg")

		#cropping images and setting it in grayscale
		print 'Modeling Face'

		sub_data = i     #These are sub data sets of folder, for my faces I've used my name

		path = os.path.join(datasets, sub_data)
		if not os.path.isdir(path):
		    os.mkdir(path)

		itr = 1
		while itr < count: 
		    im = cv2.imread("orgImg/"+i+"/"+str(itr)+".jpg")
		    print "orgImg/"+i+"/"+str(itr)+".jpg"
		    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
		    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
		    for (x,y,w,h) in faces:
		        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
		        face = gray[y:y + h, x:x + w]
		        face_resize = cv2.resize(face, (width, height))
		        cv2.imwrite('%s/%s.png' % (path,itr), face_resize)
		    itr += 1
print 'done'
