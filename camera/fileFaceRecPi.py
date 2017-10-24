#faceRec for pi camera
import cv2, sys, numpy, os, picamera
import simplejson as json
from time import sleep
from picamera.array import PiRGBArray

size = 4
haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'datasets'

# Part 1: Create fisherRecognizer
print('Training...')

# Create a list of images and a list of corresponding names
(images, labels, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(datasets):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(datasets, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            label = id
            images.append(cv2.imread(path, 0))
            labels.append(int(label))
        id += 1
(width, height) = (130, 100)

# Create a Numpy array from the two lists above
(images, labels) = [numpy.array(lis) for lis in [images, labels]]

# OpenCV trains a model from the images
# NOTE FOR OpenCV2: remove '.face'
model = cv2.createFisherFaceRecognizer()
model.train(images, labels)
print 'Trained Model'
print names

# Part 2: Use fisherRecognizer on camera strea
face_cascade = cv2.CascadeClassifier(haar_file)
camera = picamera.PiCamera()
camera.vflip = True
def checkFace():
	camera.capture('face.jpg')
	im = cv2.imread('face.jpg')
	#sleep(1)
	gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
		face = gray[y:y + h, x:x + w]
		face_resize = cv2.resize(face, (width, height))
		#Try to recognize the face
		prediction = model.predict(face_resize)
		#cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)

		if prediction[1]<500:
			#cv2.putText(im,'%s - %.0f' % (names[prediction[0]],prediction[1]),(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
			print names[prediction[0]],'with ',prediction[1]
			return names[prediction[0]]
	return 'none'
            

while 1:
    x=raw_input()
    if(x=='y'):
        print checkFace()
    else:
        break