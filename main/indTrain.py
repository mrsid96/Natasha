import cv2, sys, numpy, os
from time import sleep
sub_data,y=raw_input("user img").split()
haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'datasets'  #All the faces data will be present this folder

path = os.path.join(datasets, sub_data)
if not os.path.isdir(path):
    os.mkdir(path)
(width, height) = (130, 100)

DIR = 'datasets/'+sub_data+'/'
count = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])


face_cascade = cv2.CascadeClassifier(haar_file)

im = cv2.imread(y)
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 4)
for (x,y,w,h) in faces:
    cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
    face = gray[y:y + h, x:x + w]
    face_resize = cv2.resize(face, (width, height))
    cv2.imwrite('%s/%s.png' % (path,count), face_resize)